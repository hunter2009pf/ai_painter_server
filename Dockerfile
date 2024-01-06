FROM artifacts.iflytek.com/docker-private/cbg_im/python:3.11

WORKDIR /ai_painter

COPY . .

# 设置python国内镜像
RUN python3 --version
RUN python3 -m pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
# RUN python3 -m pip install diffusers-0.25.0-py3-none-any.whl
RUN python3 -m pip install -r requirements.txt

CMD ./ai_painter_run.sh
