'''
Author: hunter2009pf angel_clothes@outlook.com
Date: 2023-12-31 21:32:35
LastEditors: hunter2009pf angel_clothes@outlook.com
LastEditTime: 2024-01-01 09:42:18
FilePath: \ai_painter\client\demo.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
from io import BytesIO
from PIL import Image
import gradio as gr
import requests


AI_PAINT_SERVER_ADDRESS = "http://127.0.0.1:28888"

def generate_image_by_prompt(prompt :str):
    resp = requests.get(
        f'{AI_PAINT_SERVER_ADDRESS}/api/v1/paint/text2img', 
        params={"prompt": prompt},
    )
    my_img = Image.open(BytesIO(resp.content))
    return my_img

demo = gr.Interface(
    fn=generate_image_by_prompt, 
    inputs=["text"],
    outputs=["image"],
)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7890,
    )
