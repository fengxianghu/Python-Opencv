# 模型1: RGB 模型,三维坐标
# 每个维度代表一种颜色
# 每个维度0-255 空间中没一点代表的是RGB混合的颜色
# 模型2: HSV  原本H方向是360，但是在Opencv的H方向的取值是0-180(归一化) H: 0-180 S: 0-255 V:0-255
# HIS,YCrCb, YUV(Linux)
# 色彩空间是可以互相转换

import cv2 as cv
import numpy as np
## 色彩空间转换 API ->非常重要
# 似乎在视频中是不考虑通道的问题
def color_follow():
    capture = cv.VideoCapture("D:\\Onedrive\\Documents\\codes\\Script1.flv")
    while(True):
        ret,frame = capture.read()
        if ret == False:
            break;
        lower = np.array([0, 43, 46])
        upper = np.array([10, 255, 255])
        HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        #Checks if array elements lie between the elements of two other arrays.
        result = cv.inRange(HSV, lower, upper)
        dst = cv.bitwise_and(frame,frame,mask=result)# 提取动的那个部分，且显示颜色
        cv.imshow("video1",frame)
        cv.imshow("video2",result)
        cv.imshow("video3", dst)
        c = cv.waitKey(1000)
        if c == 27:
            break;


def color_space_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow("gray",gray)
    HSV = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow("HSV", HSV)
    YCrCb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.imshow("HSV", HSV)

print("--------------------Hi, Python------------------------------")
src = cv.imread("D:\\Onedrive\\Bilder\\chen.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# 创建窗口的namedWindow default parameter为WINDOW_AUTOSIZE。窗口大小会自动调整以适应所显示的图像，但是不能更改大小
cv.imshow("input image", src)
color_space_demo(src)
color_follow()
b,g,r = cv.split(src) # 通道分离与合并
m =  cv.merge(b,g,r)
cv.waitKey(0)  # 无限制等待用户的按键事件
cv.destroyAllWindows()

    # 导入后，图片就会变成变成numpy


    #算数运算- 加减乘除 应用它-调节对比度 调整对比度
    # 逻辑运算:与或非,应用遮罩层控制