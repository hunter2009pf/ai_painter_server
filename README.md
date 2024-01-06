# ai_painter_server
A server that provides text2img and img2img service.

## start service in docker container
```
docker build -t ai_painter:release_20240101_1 .
docker run --name ai_painter_docker -d -p 17890:7890 -e AI_PAINTER_ENVIRONMENT=release ai_painter:release_20240101_1
```

## Q&A
1. hugging face国内镜像：https://hf-mirror.com/
2. 国内模型网站：https://modelscope.cn/my/overview
3. 如何用huggingface-cli下载模型？
    ```
    huggingface-cli download --resume-download stabilityai/stable-diffusion-xl-base-1.0 --local-dir E:/ai_painting/ai_painter_server/models/stable_diffusion/stable-diffusion-xl-base-1.0
    huggingface-cli download --resume-download stabilityai/stable-diffusion-xl-refiner-1.0 --local-dir E:/ai_painting/ai_painter_server/models/stable_diffusion/stable-diffusion-xl-refiner-1.0
    ```
4. 如何用huggingface-cli下载某个文件，并缓存到指定文件夹？
   ```
    # huggingface-cli download <仓库名> <文件名> --cache-dir <缓存文件夹路径>
    huggingface-cli download stabilityai/stable-diffusion-xl-base-1.0 sd_xl_base_1.0.safetensors --cache-dir /data/feipan3/ai_paint/model_cache
   ```
