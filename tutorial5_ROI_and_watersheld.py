import cv2 as cv
import numpy as np #针对数组操作的包


#ROI(Region of interest)  也就是找出感兴趣的那个为主

print("--------------------Hi, Python------------------------------")
src = cv.imread("D:\\Onedrive\\Bilder\\chen.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# 创建窗口的namedWindow default parameter为WINDOW_AUTOSIZE。窗口大小会自动调整以适应所显示的图像，但是不能更改大小
cv.imshow("input image",src)
getpart = src[200:300,100:500]# 似乎这个感兴趣的都是人为手动的操作
src[200:300,100:500] = cv.cvtColor(cv.cvtColor(getpart,cv.COLOR_BGR2GRAY),cv.COLOR_GRAY2BGR)
cv.imshow("recover",src)
cv.waitKey(0) # 无限制等待用户的按键事件
cv.destroyAllWindows()

# 导入后，图片就会变成变成numpy