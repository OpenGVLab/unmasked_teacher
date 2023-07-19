from configs.data import *
from configs.model import *

# ========================= data ==========================
train_corpus = "data_25m"
train_file = "${available_corpus[${train_corpus}]}"  # for lazy evaluation
test_file = dict(msrvtt_1k_test=available_corpus["msrvtt_1k_test"])
test_types = ["msrvtt_1k_test"]
num_workers = 12

stop_key = None

# ========================= input ==========================
num_frames = 4
num_frames_test = 4
batch_size = 128
max_txt_l = 32

inputs = dict(
    image_res=224,
    video_input=dict(
        num_frames="${num_frames}",
        sample_type="rand",
        num_frames_test="${num_frames_test}",
        sample_type_test="middle",
        random_aug=False,
    ),
    max_txt_l=dict(image="${max_txt_l}", video="${max_txt_l}"),
    batch_size=dict(image="${batch_size}", video="${batch_size}"),
    batch_size_test=dict(image="${batch_size}", video="${batch_size}"),
)

# ========================= model ==========================
text_enc = "bert_large"
model = dict(
    model_cls="UMT",
    vision_encoder=dict(
        # backbone
        name="vit_l14",
        img_size=224, 
        patch_size=16, 
        d_model=1024,
        encoder_embed_dim=1024, 
        encoder_depth=24,
        encoder_num_heads=16, 
        drop_path_rate=0.2, 
        num_frames="${num_frames}",
        tubelet_size=1,
        use_checkpoint=False,
        checkpoint_num=12,
        clip_decoder_embed_dim=1024,
        clip_output_dim=768,
        clip_return_layer=6,
        clip_student_return_interval=1,
        pretrained="your_model_path/l16_ptk710_f8_res224.pth",
        # clip teacher
        clip_teacher="clip_l14",
        clip_img_size=196,
        clip_return_interval=1,
        # mask
        video_mask_type="attention",
        video_mask_ratio=0.8,
        video_double_mask_ratio=0.,
        image_mask_type="attention",
        image_mask_ratio=0.5,
        image_double_mask_ratio=0.,
        # for ret
        keep_temporal=True,
    ),
    text_encoder="${TextEncoders[${text_enc}]}",
    multimodal=dict(enable=True),
    embed_dim=768,
    temp=0.07,
)

criterion = dict(
    loss_weight=dict(
        vtc=1.0, 
        mlm=1.0, 
        vtm=1.0, 
        uta=1.0,
    ),  # 0: disabled.
    vtm_hard_neg=True,
    mlm_masking_prob=0.5,
    uta_norm_type="l2",
    uta_loss_type="l2",
)

optimizer = dict(
    opt="adamW",
    lr=1e-4,
    opt_betas=[0.9, 0.999],  # default
    weight_decay=0.02,
    max_grad_norm=-1,  # requires a positive float, use -1 to disable
    # use a different lr for some modules, e.g., larger lr for new modules
    different_lr=dict(enable=False, module_names=[], lr=1e-3),
)

scheduler = dict(sched="cosine", epochs=10, min_lr_multi=0.01, warmup_epochs=1)

evaluate = False
deep_fusion = False
evaluation = dict(
    eval_frame_ensemble="concat",  # [concat, max, mean, lse]
    eval_x_only=False,
    k_test=128,
    eval_offload=True,  # offload gpu tensors to cpu to save memory.
)

fp16 = True
gradient_checkpointing = True

# ========================= wandb ==========================
wandb = dict(
    enable=True,
    entity="user",  # username or team name to store the runs, see https://docs.wandb.ai/ref/python/init
    project="umt",  # setup in your command line
)
dist_url = "env://"
device = "cuda"
mode = "pt"

# ========================= others ==========================
output_dir = None  # output dir
resume = False  # if True, load optimizer and scheduler states as well
debug = False
log_freq = 100
seed = 42

save_latest = True
auto_resume = True
pretrained_path = ""  # path to pretrained model weights, for resume only?
