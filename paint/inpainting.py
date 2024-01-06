'''
Author: hunter2009pf angel_clothes@outlook.com
Date: 2023-12-31 10:13:23
LastEditors: hunter2009pf angel_clothes@outlook.com
LastEditTime: 2023-12-31 17:55:37
FilePath: \ai_painter\paint\inpainting.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
from diffusers import AutoPipelineForInpainting
from PIL.Image import Image
import torch

from paint.base_painter import BasePainter


class InPaintingPainter(BasePainter):
    def __init__(self, model_dir_path :str, model_path :str=""):
        super().__init__(model_dir_path=model_dir_path, model_path=model_path)
        # use from_pipe to avoid consuming additional memory when loading a checkpoint
        self.pipeline = AutoPipelineForInpainting.from_pretrained(
             model_dir_path, 
             torch_dtype=torch.float16, 
             variant="fp16", 
             use_safetensors=True,
        ).to("cuda")
    
    def draw(self, init_image_path :str, mask_image_path :str, prompt :str) -> Image:
        init_image = Image.open(init_image_path)
        mask_image = Image.open(mask_image_path)
        image = self.pipeline(prompt=prompt, image=init_image, mask_image=mask_image, strength=0.85, guidance_scale=12.5).images[0]
        return image