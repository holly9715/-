#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/12 14:07
# @Author  : 剑客阿良_ALiang
# @Site    :
# @File    : video_tool.py

import os
import uuid
from ffmpy import FFmpeg


# 调整视频大小
def change_size(video_path: str, output_dir: str, width: int, height: int, bit_rate=2000):
    ext = os.path.basename(video_path).strip().split('.')[-1]
    if ext not in ['mp4']:
        raise Exception('format error')
    _result_path = os.path.join(
        output_dir, '{}.{}'.format(
            uuid.uuid1().hex, ext))
    ff = FFmpeg(executable="D:\\python\\Lib\\site-packages\\imageio_ffmpeg\\binaries\\ffmpeg-win64-v4.2.2.exe", inputs={'{}'.format(video_path): None}, outputs={
        _result_path: '-s {}*{} -b {}k'.format(width, height, bit_rate)})
    print(ff.cmd)
    ff.run()
    return _result_path


if __name__ == '__main__':
    print(change_size("D:\\code\\好玩\\媒体1.mp4", 'D:\\code\\好玩', 400, 200))
