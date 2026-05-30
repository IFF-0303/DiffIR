# DiffIR: Efficient Diffusion Model for Image Restoration (ICCV 2023)

[Paper](https://arxiv.org/pdf/2303.09472.pdf) | [Project Page](https://github.com/Zj-BinXia/DiffIR) | [Pretrained Models](https://drive.google.com/drive/folders/10miVILiopE414GyaSZM3EFAZITeY9q0p?usp=sharing)

DiffIR is an efficient diffusion-based image restoration framework. Instead of repeatedly denoising entire images or feature maps, DiffIR estimates a compact image prior representation (IPR) and uses it to guide restoration. The repository covers inpainting, GAN-based single-image super-resolution, real-world super-resolution, and motion deblurring experiments.

## Highlights

- **Two-stage restoration pipeline:** first pretrains CPEN/DIRformer with ground-truth guidance, then trains a diffusion model to estimate the compact IPR from low-quality inputs.
- **Efficient diffusion target:** predicts compact prior vectors rather than full images, reducing sampling iterations and computation.
- **Multi-task coverage:** provides task-specific training, testing, pretrained weights, and reported results for four restoration settings.

## News

- **Dec 19, 2023:** Reference-based DiffIR (DiffRIR) was released to reduce texture, brightness, and contrast disparities in editing tasks such as inpainting and outpainting. Code and pretrained models are available at [DiffRIR](https://github.com/Zj-BinXia/DiffRIR).
- **Sep 10, 2023:** Released x1 and x2 pretrained models for real-world super-resolution.
- **Sep 6, 2023:** Added real-world SR/SRGAN support for testing [LR images without GT images](DiffIR-RealSR/options/test_DiffIRS2_GAN_x4.yml) and [inference](DiffIR-RealSR/inference_diffir.py).
- **Aug 31, 2023:** Updated 2x SR training files for real-world SR and SRGAN tasks.
- **Aug 28, 2023:** Released [RealworldSR-DiffIRS2-GANV2 pretrained models](https://drive.google.com/drive/folders/1H4DU-9fB15fSz-OFko00HlWYbNSqmAKq?usp=sharing) and [training files](DiffIR-RealSR/options/train_DiffIRS2_GAN_x4_V2.yml) focused more on perceptual quality than distortion.
- **Jul 20, 2023:** Released training/testing code and pretrained models.

## Method Summary

> DiffIR is designed for restoration tasks where outputs must remain consistent with the ground truth. It uses a compact IR prior extraction network (CPEN), dynamic IR transformer (DIRformer), and denoising network. Stage 1 learns a compact image prior representation from ground-truth images; Stage 2 trains a diffusion model to estimate that prior from low-quality inputs. Because the diffusion target is compact, DiffIR can use fewer iterations while producing stable and realistic restorations.

<p align="center">
  <img width="800" src="figs/method.jpg" alt="DiffIR method overview">
</p>

## Repository Layout

| Path | Purpose |
| --- | --- |
| `DiffIR-inpainting/` | Inpainting training, evaluation, configs, model code, data preparation, and pretrained-model usage notes. |
| `figs/` | Figures used by the project README, including method and result visualizations. |
| `DiffIR-SRGAN/` | GAN-based single-image super-resolution code and docs when present in a full checkout. |
| `DiffIR-RealSR/` | Real-world super-resolution code and docs when present in a full checkout. |
| `DiffIR-demotionblur/` | Motion deblurring code and docs when present in a full checkout. |

> **Note:** This checkout contains the inpainting module. Some links above point to task directories that may exist only in the full upstream repository or in task-specific releases.

## Installation

Install dependencies from the task directory you plan to run:

| Task | Installation Entry Point |
| --- | --- |
| Inpainting | [`DiffIR-inpainting/pip.sh`](DiffIR-inpainting/pip.sh) |
| GAN-based single-image super-resolution | `DiffIR-SRGAN/pip.sh` |
| Real-world super-resolution | `DiffIR-RealSR/pip.sh` |
| Motion deblurring | `DiffIR-demotionblur/pip.sh` |

## Training, Evaluation, and Models

Task-specific instructions live in each task directory. Use the table below for quick navigation.

| Task | Training | Evaluation | Pretrained Models |
| --- | --- | --- | --- |
| Inpainting | [Instructions](DiffIR-inpainting/README.md#training) | [Instructions](DiffIR-inpainting/README.md#evaluation) | [Download](https://drive.google.com/drive/folders/1RQXRWMqVaAsyyQt8T-3KtpS68ef8dh90?usp=drive_link) |
| GAN-based single-image super-resolution | [Instructions](DiffIR-SRGAN/README.md#training) | [Instructions](DiffIR-SRGAN/README.md#evaluation) | [Download](https://drive.google.com/drive/folders/1Mmhz6Sx9tz-n3QJAd6w-UlxdugTEH2fV?usp=drive_link) |
| Real-world super-resolution | [Instructions](DiffIR-RealSR/README.md#training) | [Instructions](DiffIR-RealSR/README.md#evaluation) | [Download](https://drive.google.com/drive/folders/1G3Ep0xd-uBpIXGZFdWzH1uVCOpJaqkOF?usp=drive_link) |
| Motion deblurring | [Instructions](DiffIR-demotionblur/README.md#training) | [Instructions](DiffIR-demotionblur/README.md#evaluation) | [Download](https://drive.google.com/drive/folders/1JWYaP9VVPX_Mh2w1Vezn74hck-oWSyMh?usp=drive_link) |

## Results

Experiments cover inpainting, GAN-based single-image super-resolution, real-world super-resolution, and motion deblurring.

<details>
<summary><strong>Inpainting</strong> (click to expand)</summary>

<img src="figs/inpainting-quan.jpg" alt="Inpainting quantitative results">
<img src="figs/inpainting-qual.jpg" alt="Inpainting qualitative results">

</details>

<details>
<summary><strong>GAN-based single-image super-resolution</strong> (click to expand)</summary>

<img src="figs/SISR-quan.jpg" alt="GAN-based SISR quantitative results">
<img src="figs/SISR-qual.jpg" alt="GAN-based SISR qualitative results">

</details>

<details>
<summary><strong>Real-world super-resolution</strong> (click to expand)</summary>

<img src="figs/realworldsr-quan.jpg" alt="Real-world SR quantitative results">
<img src="figs/realworldsr-qual.jpg" alt="Real-world SR qualitative results">

</details>

<details>
<summary><strong>Motion deblurring</strong> (click to expand)</summary>

<img src="figs/deblur-quan.jpg" alt="Motion deblurring quantitative results">
<img src="figs/deblur-qual.jpg" alt="Motion deblurring qualitative results">

</details>

## Citation

If you use DiffIR, please cite:

```bibtex
@article{xia2023diffir,
  title={Diffir: Efficient diffusion model for image restoration},
  author={Xia, Bin and Zhang, Yulun and Wang, Shiyin and Wang, Yitong and Wu, Xinglong and Tian, Yapeng and Yang, Wenming and Van Gool, Luc},
  journal={ICCV},
  year={2023}
}
```

## Contact

For questions, contact <zjbinxia@gmail.com>.
