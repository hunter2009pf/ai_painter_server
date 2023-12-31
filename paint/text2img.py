'''
Author: hunter2009pf angel_clothes@outlook.com
Date: 2023-12-31 10:13:23
LastEditors: hunter2009pf angel_clothes@outlook.com
LastEditTime: 2023-12-31 22:10:31
FilePath: \ai_painter\paint\text2img.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
from diffusers import AutoPipelineForText2Image
from PIL import Image
import torch

from paint.base_painter import BasePainter


class Text2ImgPainter(BasePainter):
    def __init__(self, model_dir_path :str, model_path :str=""):
        super().__init__(model_dir_path=model_dir_path, model_path=model_path)
        self.pipeline = AutoPipelineForText2Image.from_pretrained(
            model_dir_path,
            torch_dtype=torch.float16, 
            variant="fp16",
        ).to("cuda")
    
    def draw(self, prompt :str="Astronaut in a jungle, cold color palette, muted colors, detailed, 8k") -> Image:
        image = self.pipeline(prompt=prompt, num_inference_steps=1, guidance_scale=0.0).images[0]
        return image


text2img_painter = Text2ImgPainter(
    model_dir_path="/data/feipan3/ai_paint/model_cache/models--stabilityai--sdxl-turbo/snapshots/f4b0486b498f84668e828044de1d0c8ba486e05b"
)
