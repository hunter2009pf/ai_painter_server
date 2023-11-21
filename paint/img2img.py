from diffusers import AutoPipelineForImage2Image
from diffusers.utils import load_image
import torch
import PIL


class Img2Img:
    @classmethod
    def paint(cls, model_path :str, init_image :PIL.Image.Image, prompt :str):
        # use from_pipe to avoid consuming additional memory when loading a checkpoint
        pipeline = AutoPipelineForImage2Image.from_pretrained(
            model_path, torch_dtype=torch.float16, variant="fp16", use_safetensors=True
        ).to("cuda")
        image = pipeline(prompt, image=init_image, strength=0.8, guidance_scale=10.5).images[0]
        image.save('E:/ai_painting/test1.png')