import os
import uvicorn

from fastapi.middleware.cors import CORSMiddleware
from configs.config import settings, parser
from api.http_handler import app

def start_service():
    # os.environ["TOKENIZERS_PARALLELISM"] = "true"
    parser.add_argument("--host", type=str, default="0.0.0.0")
    parser.add_argument("--port", type=int, default=settings.SERVICE.PORT)
    # 初始化消息
    args = parser.parse_args()

    # Add CORS middleware to allow all origins
    # 在config.py中设置OPEN_DOMAIN=True，允许跨域
    # set OPEN_DOMAIN=True in config.py to allow cross-domain
    if settings.OPEN_CROSS_DOMAIN:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    
    uvicorn.run(app, host=args.host, port=args.port)
