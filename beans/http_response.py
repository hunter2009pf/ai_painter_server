'''
Author: hunter2009pf angel_clothes@outlook.com
Date: 2023-12-31 20:09:07
LastEditors: hunter2009pf angel_clothes@outlook.com
LastEditTime: 2023-12-31 20:37:59
FilePath: \ai_painter\beans\http_response.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
import pydantic
from pydantic import BaseModel
from constants.custom_response_code import CustomResponseCode


class BaseResponse(BaseModel):
    code: int = pydantic.Field(CustomResponseCode.CODE_SUCCESS, description="response status code")
    msg: str = pydantic.Field("success", description="response status message")

    class Config:
        json_schema_extra = {
            "example": {
                "code": CustomResponseCode.CODE_SUCCESS,
                "msg": "成功",
            }
        }
        
class VersionResponse(BaseResponse):
    data: dict = pydantic.Field(default={}, description="single document info")

    class Config:
        json_schema_extra = {
            "example": {
                "code": CustomResponseCode.CODE_SUCCESS,
                "msg": "success",
                "data": {
                    "version": "v1.0"
                },
            }
        }

class SingleDocumentResponse(BaseResponse):
    data: dict = pydantic.Field(default={}, description="single document info")

    class Config:
        schema_extra = {
            "example": {
                "code": CustomResponseCode.CODE_SUCCESS,
                "msg": "success",
                "data": {
                    "file_name": "hello_world.txt",
                    "is_pure_text": False,
                    "file_path": "/content/feipan3/123/hello_world.txt"
                },
            }
        }
