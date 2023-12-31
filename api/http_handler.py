import os

from fastapi import FastAPI, Query
from fastapi.responses import RedirectResponse, FileResponse

from beans.http_response import VersionResponse
from constants.custom_response_code import CustomResponseCode
from constants.constants import *
from constants.custom_url import CustomUrl
from paint.text2img import text2img_painter
from utils.path_util import PathUtil


app = FastAPI()

# get API documentation
@app.get(CustomUrl.ROOT)
def get_api_document():
    return RedirectResponse(url=CustomUrl.DOCS)


# 获取版本
@app.get(CustomUrl.GET_VERSION)
def get_version() -> VersionResponse:
    return VersionResponse(
        code=CustomResponseCode.CODE_SUCCESS,
        msg="success",
        data={
            "version": VERSION
        }
    )
    
# 文生图
@app.get(CustomUrl.TEXT_TO_IMAGE)
def generate_image_by_prompt(
    prompt :str = Query(..., description="想生成什么样的图片，用提示词表述", examples=["一只飞翔的可爱山羊，背上有一个数字3"]),    
) -> FileResponse:
    image = text2img_painter.draw(prompt=prompt)
    saved_path = os.path.join(PathUtil.get_image_saved_dir_path(), "text2img_result0.png")
    image.save(saved_path)
    return FileResponse(
        saved_path
    )
    
    # saved_path  = "C:/Users/feipan3/Pictures/beauty.jpg"
    # return FileResponse(
    #     saved_path
    # )