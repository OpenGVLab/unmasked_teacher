import os
from data.ava import AVAVideoDataset
from data.transforms import TransformsCfg
import alphaction.config.paths_catalog as paths_catalog
from alphaction.dataset.collate_batch import batch_different_videos


class BatchCollator(object):
    """
    From a list of samples from the dataset,
    returns the batched objectimages and targets.
    This should be passed to the DataLoader
    """
    def __init__(self, size_divisible=0):
        self.divisible = size_divisible
        self.size_divisible = self.divisible

    def __call__(self, batch):
        transposed_batch = list(zip(*batch))
        video_data = batch_different_videos(transposed_batch[0], self.size_divisible)
        boxes = transposed_batch[1]
        video_ids = transposed_batch[2]
        return video_data, boxes, video_ids


def build_ava_dataset(is_train, transforms, frame_span=64):
    input_filename = 'ava_video_train_v2.2' if is_train else 'ava_video_val_v2.2'
    assert input_filename
    dataset_catalog = paths_catalog.DatasetCatalog

    data = dataset_catalog.get(input_filename)
    ava_args = data["args"]
    ava_args["remove_clips_without_annotations"] = is_train
    ava_args["frame_span"] = frame_span
    if not is_train:
        ava_args["box_thresh"] = 0.8  #
        ava_args["action_thresh"] = 0.  #
    else:
        # disable box_file when train, use only gt to train
        ava_args["box_file"] = None

    ava_args["transforms"] = transforms
    dataset = AVAVideoDataset(**ava_args)
    return dataset


