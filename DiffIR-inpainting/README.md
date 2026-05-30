# DiffIR Inpainting

This module contains the inpainting implementation of DiffIR. The code is based on [LaMa](https://github.com/advimman/lama) and includes data preparation scripts, training scripts, evaluation scripts, configs, and model code for CelebA-HQ and Places2 experiments.

## Quick Reference

| Dataset / Setting | Stage 1 Training | Stage 2 Conversion | Stage 2 Training | Testing | Metrics |
| --- | --- | --- | --- | --- | --- |
| CelebA-HQ | `sh train_celebahqS1.sh` | `python3 S1forS2.py` | `sh train_celebahqS2.sh` | `sh test_celeba_256_thick.sh` | `sh eval_celeba_256_thick.sh` |
| Places2 Standard | `sh train_place256S1.sh` | `python3 S1forS2.py` | `sh train_place256S2.sh` | `sh test_place2_512_thick.sh` | `sh eval_place2_512_thick.sh` |
| Places2 Challenge | `sh train_place256_bigLdataS1.sh` | `python3 S1forS2.py` | `sh train_place256_bigLdataS2.sh` | `sh test_place2_512_thick_big.sh` | `sh eval_place2_512_thick_big.sh` |

## Training

### 1. Prepare Training and Testing Data

#### Places2 Dataset

Download the Places365-Standard high-resolution train, validation, and test archives from <http://places2.csail.mit.edu/download.html>:

```bash
wget http://data.csail.mit.edu/places/places365/train_large_places365standard.tar
wget http://data.csail.mit.edu/places/places365/val_large.tar
wget http://data.csail.mit.edu/places/places365/test_large.tar
```

Unpack the train/test/validation data and create dataset configs:

```bash
bash fetch_data/places_standard_train_prepare.sh
bash fetch_data/places_standard_test_val_prepare.sh
```

Sample validation/test images and generate masks for visualization and end-of-epoch testing:

```bash
bash fetch_data/places_standard_test_val_sample.sh
bash fetch_data/places_standard_test_val_gen_masks.sh
```

Prepare the held-out 30k-image evaluation split and masks used for paper-style metrics:

```bash
bash fetch_data/places_standard_evaluation_prepare_data.sh
```

#### CelebA-HQ Dataset

Set the working environment from the LaMa/DiffIR inpainting directory:

```bash
export TORCH_HOME=$(pwd)
export PYTHONPATH=$(pwd)
```

Download `data256x256.zip` from either of the following links:

- <https://drive.google.com/drive/folders/11Vz0fqHS2rXDb5pprgTjpD7S2BAJhi1P>
- <https://drive.google.com/file/d/1foD5VnGxBJOg8N__OesoDuYY4DyUL-xE/view?usp=drive_link>

Unzip and split the data into train/test/visualization sets, then create configs:

```bash
bash fetch_data/celebahq_dataset_prepare.sh
```

Generate masks for test and visual-test sets:

```bash
bash fetch_data/celebahq_gen_masks.sh
```

### 2. Train Models

DiffIR training uses two stages:

1. **Stage 1:** Train DiffIR-S1 to learn the restoration prior with ground-truth guidance.
2. **Stage 2:** Convert the Stage 1 checkpoint with `S1forS2.py`, update the Stage 2 config paths, then train DiffIR-S2.

#### 2.1 CelebA-HQ

Train DiffIR-S1:

```bash
sh train_celebahqS1.sh
```

Convert the pretrained DiffIR-S1 checkpoint:

```bash
# Edit the `path` item in S1forS2.py so it points to the DiffIR-S1 checkpoint.
# The conversion produces celeba-S1.pth.
python3 S1forS2.py
```

Train DiffIR-S2:

```bash
# Edit `generatorS2_path` and `generatorS1_path` in configs/training/DiffIRS2-celeba.yaml
# so both point to celeba-S1.pth.
sh train_celebahqS2.sh
```

#### 2.2 Places2 Standard

Train DiffIR-S1:

```bash
sh train_place256S1.sh
```

Convert the pretrained DiffIR-S1 checkpoint:

```bash
# Edit the `path` item in S1forS2.py so it points to the DiffIR-S1 checkpoint.
# The conversion produces place-S1.pth.
python3 S1forS2.py
```

Train DiffIR-S2:

```bash
# Edit `generatorS2_path` and `generatorS1_path` in configs/training/DiffIRS2-place2.yaml
# so both point to place-S1.pth.
sh train_place256S2.sh
```

#### 2.3 Places2 Challenge

Train DiffIR-S1:

```bash
sh train_place256_bigLdataS1.sh
```

Convert the pretrained DiffIR-S1 checkpoint:

```bash
# Edit the `path` item in S1forS2.py so it points to the DiffIR-S1 checkpoint.
# The conversion produces placebigdata-S1.pth.
python3 S1forS2.py
```

Train DiffIR-S2:

```bash
# Edit `generatorS2_path` and `generatorS1_path` in configs/training/DiffIRbigdataS2-place2.yaml
# so both point to placebigdata-S1.pth.
sh train_place256_bigLdataS2.sh
```

> **GPU note:** The training scripts use 8 GPUs by default. To use a different number of GPUs, update the script launch arguments and dataset paths under `configs/training/location/`.

## Evaluation

Download the pretrained [inpainting model](https://drive.google.com/drive/folders/1RQXRWMqVaAsyyQt8T-3KtpS68ef8dh90?usp=drive_link) and place it under `./experiments/`.

### CelebA-HQ

Run testing:

```bash
sh test_celeba_256_thick.sh
```

Calculate metrics:

```bash
sh eval_celeba_256_thick.sh
```

### Places2 Standard

Run testing:

```bash
sh test_place2_512_thick.sh
```

Calculate metrics:

```bash
sh eval_place2_512_thick.sh
```

### Places2 Challenge

Run testing:

```bash
sh test_place2_512_thick_big.sh
```

Calculate metrics:

```bash
sh eval_place2_512_thick_big.sh
```
