# ai_painter_server
A server that provides text2img and img2img service.

## Q&A
1. hugging face国内镜像：https://hf-mirror.com/
2. 如何用huggingface-cli下载模型？
    ```
    huggingface-cli download --resume-download stabilityai/stable-diffusion-xl-base-1.0 --local-dir E:/ai_painting/ai_painter_server/models/stable_diffusion/stable-diffusion-xl-base-1.0
    huggingface-cli download --resume-download stabilityai/stable-diffusion-xl-refiner-1.0 --local-dir E:/ai_painting/ai_painter_server/models/stable_diffusion/stable-diffusion-xl-refiner-1.0
    ```