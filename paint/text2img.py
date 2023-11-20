from diffusers import AutoPipelineForText2Image
import torch

class Text2Img:
    @classmethod
    def paint(cls, model_path :str, prompt :str="Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"):
        pipeline_text2image = AutoPipelineForText2Image.from_pretrained(
            model_path, torch_dtype=torch.float16, variant="fp16", use_safetensors=True
        ).to("cuda")
        image = pipeline_text2image(prompt=prompt).images[0]
        image.save('E:/ai_painting/test0.png')