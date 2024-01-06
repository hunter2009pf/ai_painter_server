#!/bin/bash

echo 'start running ai painter'
export CUDA_VISIBLE_DEVICES=1
nohup python main.py &
cd client
python demo.py
