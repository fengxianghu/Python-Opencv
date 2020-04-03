import cv2 as cv
import numpy as np

# 当有椒盐噪声，用中值模糊效果会很好，但是一般噪声用均值也可以

def blur_demo(image):
    dst = cv.blur(image,(1,3))
    cv.imshow("blurred_image",image)

def medien_blur_demo(image):
    dst = cv.medianBlur(image,5)
    cv.imshow("median_blurred_image",image)

#lablace 算子的作用就是锐化，其实就是求了两次导数
def custom_blur_demo(image):
    # kernel = np.ones((5,5),np.float32)/25
     kernel = np.array([[1,1,1],[1,1,1],[1,1,1]], np.float32)
     dst = cv.filter2D(image,-1,kernel=kernel)
     cv.imshow("custom_blur_demo",dst)

print("--------------------Hi, Python------------------------------")
src = cv.imread("D:\\Onedrive\\Bilder\\chen.jpg")
#cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
blur_demo(src)
# 创建窗口的namedWindow default parameter为WINDOW_AUTOSIZE。窗口大小会自动调整以适应所显示的图像，但是不能更改大小
"""""
cv.imshow("input image",src)
getpart = src[200:300,100:500]# 似乎这个感兴趣的都是人为手动的操作
src[200:300,100:500] = cv.cvtColor(cv.cvtColor(getpart,cv.COLOR_BGR2GRAY),cv.COLOR_GRAY2BGR)
cv.imshow("recover",src)
"""""

cv.waitKey(0) # 无限制等待用户的按键事件
cv.destroyAllWindows()

# 导入后，图片就会变成变成numpy