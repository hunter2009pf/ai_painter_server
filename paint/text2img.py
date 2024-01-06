'''
Author: hunter2009pf angel_clothes@outlook.com
Date: 2023-12-31 10:13:23
LastEditors: hunter2009pf angel_clothes@outlook.com
LastEditTime: 2024-01-01 10:12:26
FilePath: \ai_painter\paint\text2img.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
from diffusers import AutoPipelineForText2Image, StableDiffusionXLPipeline
from PIL import Image
import torch

from paint.base_painter import BasePainter
from utils.log_util import logger


class Text2ImgPainter(BasePainter):
    def __init__(self, model_dir_path :str = "", model_path :str = "", is_sd_xl_turbo :bool = False):
        super().__init__(model_dir_path=model_dir_path, model_path=model_path)
        self.is_sd_xl_turbo = is_sd_xl_turbo
        if model_dir_path == "" and model_path == "":
            logger.warning("must specify model path or directory when initializing Text2ImgPainter instance")
        elif model_path != "":
            self.pipeline = StableDiffusionXLPipeline.from_single_file(
                model_path, 
                torch_dtype=torch.float16, 
                variant="fp16", 
                use_safetensors=True,
            ).to("cuda")
        else:
            self.pipeline = AutoPipelineForText2Image.from_pretrained(
                model_dir_path,
                torch_dtype=torch.float16, 
                variant="fp16",
            ).to("cuda")
    
    def draw(self, prompt :str="Astronaut in a jungle, cold color palette, muted colors, detailed, 8k") -> Image:
        if self.is_sd_xl_turbo:
            image = self.pipeline(prompt=prompt, num_inference_steps=1, guidance_scale=0.0).images[0]
        else:
            image = self.pipeline(prompt=prompt).images[0]
        return image


text2img_painter = Text2ImgPainter(
    # model_dir_path="/data/feipan3/ai_paint/model_cache/models--stabilityai--sdxl-turbo/snapshots/f4b0486b498f84668e828044de1d0c8ba486e05b"
    model_path="/data/feipan3/ai_paint/ai_paint_projects/ai_painter/models/stable_diffusion/sd_xl_base_1.0.safetensors",
    is_sd_xl_turbo=False,
)
