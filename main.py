from utils.log_util import logger
from paint.text2img import Text2Img

if __name__ == "__main__":
    logger.info("start AI painter service")
    Text2Img.paint(
        model_path="E:/ai_painting/ai_painter_server/models/stable_diffusion/stable-diffusion-xl-base-1.0",
        prompt="Astronaut in a jungle, cold color palette, muted colors, detailed, 8k",    
    )