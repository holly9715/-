import imageio
 
# 读取视频文件
video = imageio.get_reader('媒体1.mp4')
 
# 创建 gif 动图的写入器
gif_writer = imageio.get_writer('output.gif', mode='I')
 
# 将视频帧逐一写入 gif 动图中
for frame in video:
    gif_writer.append_data(frame)
 
# 关闭写入器
gif_writer.close()
