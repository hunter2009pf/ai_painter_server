from diffusers import AutoPipelineForImage2Image
from diffusers.utils import load_image
from PIL import Image
import torch

from paint.base_painter import BasePainter


class Img2ImgPainter(BasePainter):
    def __init__(self, model_dir_path :str, model_path :str=""):
        super().__init__(model_dir_path=model_dir_path, model_path=model_path)
        self.pipeline = AutoPipelineForImage2Image.from_pretrained(
            model_dir_path,
            torch_dtype=torch.float16, 
            variant="fp16",
        ).to("cuda")

    def draw(self, prompt :str, init_image_path :str) -> Image:
        pil_img = Image.open(init_image_path)
        init_image = load_image(pil_img).resize((512, 512))
        image = self.pipeline(prompt, image=init_image, num_inference_steps=2, strength=0.5, guidance_scale=0.0).images[0]
        return image