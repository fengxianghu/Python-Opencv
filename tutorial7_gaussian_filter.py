import cv2 as cv
import numpy as np

# 在去噪方面，高斯模糊比均值模糊效果更加好
# 滤镜一开始用的也是高斯模糊
# 权重之和为一，因为高斯分布
def clamp(a):
    if a < 0:
        return 0
    if a > 255:
        return 255
    else:
        return a


def gaussian_noise(image):
    h,w,ch = image.shape
    for row in range(h):# 对于每一个通道的每一个像素点都得加上一个随机值，这个随机值的最大数值为20
        for col in range(w):
            s = np.random.normal(0,20,3)
            #print(s)
            image[row,col,0] = clamp(image[row,col,0] + s[0]) #blue
            image[row,col,1] = clamp(image[row, col, 1]+s[1]) # Green
            image[row,col,2] = clamp(image[row, col, 2]++s[2]) # Red
    cv.imshow("gaussian_noise", image)





print("--------------------Hi, Python------------------------------")
src = cv.imread("D:\\Onedrive\\Bilder\\chen.jpg")
cv.imshow("input image",src)
gaussian_noise(src)

# 用高斯滤波之后得到的图像再用高斯filter 是无效果的
dst = cv.GaussianBlur(src,(0,0),15)
cv.imshow("Gaussian Blur",dst)
#cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
#blur_demo(src)
# 创建窗口的namedWindow default parameter为WINDOW_AUTOSIZE。窗口大小会自动调整以适应所显示的图像，但是不能更改大小
"""""
cv.imshow("input image",src)
getpart = src[200:300,100:500]# 似乎这个感兴趣的都是人为手动的操作
src[200:300,100:500] = cv.cvtColor(cv.cvtColor(getpart,cv.COLOR_BGR2GRAY),cv.COLOR_GRAY2BGR)
cv.imshow("recover",src)
"""""

cv.waitKey(0) # 无限制等待用户的按键事件
cv.destroyAllWindows()