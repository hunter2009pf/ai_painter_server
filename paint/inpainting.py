from diffusers import AutoPipelineForInpainting
from diffusers.utils import load_image
import torch
from PIL.Image import Image


class InPainting:
    @classmethod
    def paint(cls, model_path :str, init_image :Image, mask_image :Image, prompt :str):
        # use from_pipe to avoid consuming additional memory when loading a checkpoint
        pipeline = AutoPipelineForInpainting.from_pretrained(
             model_path, torch_dtype=torch.float16, variant="fp16", use_safetensors=True
        ).to("cuda")
        prompt = "A deep sea diver floating"
        image = pipeline(prompt=prompt, image=init_image, mask_image=mask_image, strength=0.85, guidance_scale=12.5).images[0]
        image.save('E:/ai_painting/test2.png')