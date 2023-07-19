import os
import torch.utils.data as data
import time
import torch
import numpy as np

from alphaction.structures.bounding_box import BoxList
from collections import defaultdict
from alphaction.utils.video_decode import av_decode_video
from alphaction.dataset.datasets.ava import NpInfoDict, NpBoxDict

import json


class AVAVideoDataset(data.Dataset):
    def __init__(self, video_root, ann_file, remove_clips_without_annotations, frame_span, box_file=None,
                 eval_file_paths={}, box_thresh=0.0, action_thresh=0.0, transforms=None):

        print('loading annotations into memory...')
        tic = time.time()
        json_dict = json.load(open(ann_file, 'r'))
        assert type(json_dict) == dict, 'annotation file format {} not supported'.format(type(json_dict))
        print('Done (t={:0.2f}s)'.format(time.time() - tic))

        self.video_root = video_root
        self.transforms = transforms
        self.frame_span = frame_span

        # These two attributes are used during ava evaluation...
        # Maybe there is a better implementation
        self.eval_file_paths = eval_file_paths
        self.action_thresh = action_thresh

        clip2ann = defaultdict(list)
        if "annotations" in json_dict:
            for ann in json_dict["annotations"]:
                action_ids = ann["action_ids"]
                one_hot = np.zeros(81, dtype=np.bool)
                one_hot[action_ids] = True
                packed_act = np.packbits(one_hot[1:])
                clip2ann[ann["image_id"]].append(dict(bbox=ann["bbox"], packed_act=packed_act))

        movies_size = {}
        clips_info = {}
        for img in json_dict["images"]:
            mov = img["movie"]
            if mov not in movies_size:
                movies_size[mov] = [img["width"], img["height"]]
            clips_info[img["id"]] = [mov, img["timestamp"]]
        self.movie_info = NpInfoDict(movies_size, value_type=np.int32)
        clip_ids = sorted(list(clips_info.keys()))

        if remove_clips_without_annotations:
            clip_ids = [clip_id for clip_id in clip_ids if clip_id in clip2ann]

        if box_file:
            # this is only for validation or testing
            # we use detected boxes, so remove clips without boxes detected.
            imgToBoxes = self.load_box_file(box_file, box_thresh)
            clip_ids = [
                img_id
                for img_id in clip_ids
                if len(imgToBoxes[img_id]) > 0
            ]
            self.det_persons = NpBoxDict(imgToBoxes, clip_ids,
                                         value_types=[("bbox", np.float32), ("score", np.float32)])
        else:
            self.det_persons = None

        self.anns = NpBoxDict(clip2ann, clip_ids, value_types=[("bbox", np.float32), ("packed_act", np.uint8)])

        clips_info = {  # key
            clip_id:
                [
                    self.movie_info.convert_key(clips_info[clip_id][0]),
                    clips_info[clip_id][1]
                ] for clip_id in clip_ids
        }
        self.clips_info = NpInfoDict(clips_info, value_type=np.int32)

    def __getitem__(self, idx):

        _, clip_info = self.clips_info[idx]

        # mov_id is the id in self.movie_info
        mov_id, timestamp = clip_info
        # movie_id is the human-readable youtube id.
        movie_id, movie_size = self.movie_info[mov_id]
        video_data = self._decode_video_data(movie_id, timestamp)

        im_w, im_h = movie_size

        if self.det_persons is None:
            # Note: During training, we only use gt. Thus we should not provide box file,
            # otherwise we will use only box file instead.

            boxes, packed_act = self.anns[idx]

            boxes_tensor = torch.as_tensor(boxes, dtype=torch.float32).reshape(-1, 4)  # guard against no boxes
            boxes = BoxList(boxes_tensor, (im_w, im_h), mode="xywh").convert("xyxy")

            # Decode the packed bits from uint8 to one hot, since AVA has 80 classes,
            # it can be exactly denoted with 10 bytes, otherwise we may need to discard some bits.
            one_hot_label = np.unpackbits(packed_act, axis=1)
            one_hot_label = torch.as_tensor(one_hot_label, dtype=torch.uint8)

            boxes.add_field("labels", one_hot_label)  # 80

        else:
            boxes, box_score = self.det_persons[idx]
            boxes_tensor = torch.as_tensor(boxes).reshape(-1, 4)
            boxes = BoxList(boxes_tensor, (im_w, im_h), mode="xywh").convert("xyxy")

            box_score_tensor = torch.as_tensor(box_score, dtype=torch.float32).reshape(-1, 1)
            boxes.add_field("scores", box_score_tensor)

        boxes = boxes.clip_to_image(remove_empty=True)

        if self.transforms is not None:
            video_data, boxes, transform_randoms = self.transforms(video_data, boxes)

        return video_data, boxes, idx

    def get_video_info(self, index):
        _, clip_info = self.clips_info[index]
        # mov_id is the id in self.movie_info
        mov_id, timestamp = clip_info
        # movie_id is the human-readable youtube id.
        movie_id, movie_size = self.movie_info[mov_id]
        w, h = movie_size
        return dict(width=w, height=h, movie=movie_id, timestamp=timestamp)

    def load_box_file(self, box_file, score_thresh=0.0):
        import json

        print('Loading box file into memory...')
        tic = time.time()
        with open(box_file, "r") as f:
            box_results = json.load(f)
        print('Done (t={:0.2f}s)'.format(time.time() - tic))

        boxImgIds = [box['image_id'] for box in box_results]

        imgToBoxes = defaultdict(list)
        for img_id, box in zip(boxImgIds, box_results):
            if box['score'] >= score_thresh:
                imgToBoxes[img_id].append(box)
        return imgToBoxes

    def _decode_video_data(self, dirname, timestamp):
        # decode target video data from segment per second.

        video_folder = os.path.join(self.video_root, dirname)
        right_span = self.frame_span//2
        left_span = self.frame_span - right_span

        #load right
        cur_t = timestamp
        right_frames = []
        while len(right_frames)<right_span:
            video_path = os.path.join(video_folder, "{}.mp4".format(cur_t))
            # frames = cv2_decode_video(video_path)
            frames = av_decode_video(video_path)
            if len(frames)==0:
                raise RuntimeError("Video {} cannot be decoded.".format(video_path))
            right_frames = right_frames+frames
            cur_t += 1

        #load left
        cur_t = timestamp-1
        left_frames = []
        while len(left_frames)<left_span:
            video_path = os.path.join(video_folder, "{}.mp4".format(cur_t))
            # frames = cv2_decode_video(video_path)
            frames = av_decode_video(video_path)
            if len(frames)==0:
                raise RuntimeError("Video {} cannot be decoded.".format(video_path))
            left_frames = frames+left_frames
            cur_t -= 1

        #adjust key frame to center, usually no need
        min_frame_num = min(len(left_frames), len(right_frames))
        frames = left_frames[-min_frame_num:] + right_frames[:min_frame_num]

        video_data = np.stack(frames)

        return video_data

    def __len__(self):
        return len(self.clips_info)

    def __repr__(self):
        fmt_str = 'Dataset ' + self.__class__.__name__ + '\n'
        fmt_str += '    Number of datapoints: {}\n'.format(self.__len__())
        fmt_str += '    Video Root Location: {}\n'.format(self.video_root)
        tmp = '    Transforms (if any): '
        fmt_str += '{0}{1}\n'.format(tmp, self.transforms.__repr__().replace('\n', '\n' + ' ' * len(tmp)))
        return fmt_str