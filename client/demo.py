from io import BytesIO
import gradio as gr
import os
import requests
from PIL import Image


def combine(a, b):
    return a + " " + b

def generate_image_by_prompt(input_img):
    resp = requests.get('http://172.31.101.127:28888/api/v1/paint/text2img', params={"prompt": "a plane flying in the blue sky, 8k"})
    my_img = Image.open(BytesIO(resp.content))
    return gr.Image(type="pil", value=my_img)


# with gr.Blocks() as demo:

#     txt = gr.Textbox(label="Input", lines=2)
#     txt_2 = gr.Textbox(label="Input 2")
#     txt_3 = gr.Textbox(value="", label="Output")
#     btn = gr.Button(value="Submit")
#     btn.click(combine, inputs=[txt, txt_2], outputs=[txt_3])

#     with gr.Row():
#         im = gr.Image(type="pil", elem_id="img_result")

#     btn = gr.Button(value="text to image")
#     btn.click(generate_image_by_prompt, outputs=[im])

#     gr.Markdown("## Text Examples")
#     gr.Examples(
#         [["hi", "Adam"], ["hello", "Eve"]],
#         [txt, txt_2],
#         txt_3,
#         combine,
#         cache_examples=True,
#     )

demo = gr.Interface(generate_image_by_prompt, gr.Image(type="pil"), "image")

if __name__ == "__main__":
    demo.launch()
