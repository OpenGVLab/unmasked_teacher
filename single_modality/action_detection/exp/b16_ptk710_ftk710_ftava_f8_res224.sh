export MASTER_PORT=$((12000 + $RANDOM % 20000))
export OMP_NUM_THREADS=1

OUTPUT_DIR="$(dirname $0)"
MODEL_PATH='your_model_path/b16_ptk710_ftk710_f8_res224.pth'

PARTITION='video'
GPUS=16
GPUS_PER_NODE=8
CPUS_PER_TASK=14

srun -p $PARTITION \
    --job-name=${JOB_NAME} \
    --gres=gpu:${GPUS_PER_NODE} \
    --ntasks=${GPUS} \
    --ntasks-per-node=${GPUS_PER_NODE} \
    --cpus-per-task=${CPUS_PER_TASK} \
    python3 -u run_class_finetuning.py \
    --model vit_base_patch16_224 \
    --finetune ${MODEL_PATH} \
    --log_dir ${OUTPUT_DIR}/logs \
    --output_dir ${OUTPUT_DIR}/models \
    --batch_size 8 \
    --input_size 224 \
    --save_ckpt_freq 10 \
    --num_frames 8 \
    --sampling_rate 8 \
    --sparse \
    --tubelet_size 1 \
    --opt adamw \
    --lr 2.5e-4 \
    --layer_decay 0.75 \
    --opt_betas 0.9 0.999 \
    --weight_decay 0.05 \
    --epochs 30 \
    --data_set "ava" \
    --drop_path 0.2 \
    --val_freq 10
