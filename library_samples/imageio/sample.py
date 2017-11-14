# coding:utf-8
import imageio

#read and write image
data = imageio.imread("./data/got1.jpg")
imageio.imwrite("./data/got1_copy.jpg",data)

# read images from video  可以指定任意视频路径
reader = imageio.get_reader("./data/vid.mp4")

#打印取视频信息
# 可以获取视频的信息包括：
# fps (每秒传输帧数)、nframes (帧数)、size(尺寸) 、duration(时长)
print reader.get_meta_data() #

#获取第一帧的数据并且保存
first_frame_data = reader.get_data(0) #获取第一帧的数据
imageio.imwrite("./data/first_frame.jpg",reader.get_data(0))

# 可迭代获取每一帧的数据
for i, im in enumerate(reader):
    print i
    print im

# 复制视频到指定位置
writer = imageio.get_writer('./data/vid_copy.mp4', fps=reader.get_meta_data()["fps"])
for frame_data in reader:
    writer.append_data(frame_data)
writer.close()