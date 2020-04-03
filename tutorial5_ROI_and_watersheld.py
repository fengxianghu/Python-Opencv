import cv2 as cv
import numpy as np #针对数组操作的包

def fill_color_demo(image):
    copyimage = image.copy()
    h,w = copyimage.shape[:2]
    mask = np.zeros((h+2,w+2),np.uint8)
    #fixed Range (100,100,100),(50,50,50)
    cv.floodFill(copyimage,mask,(30,30),(0,255,255),(100,100,100),(50,50,50),cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill_color_demo",copyimage)
#FLOODFILL_FIXED_RANGE-改变图像，泛洪填充
#FLOODFILL_MASK_ONLY-不改变图像，只填充遮罩层本身，忽略新的颜色值参数

def fill_color_demo(image):
    copyimage = image.copy()
    h,w = copyimage.shape[:2]
    mask = np.zeros((h+2,w+2),np.uint8)
    cv.floodFill(copyimage,mask,(30,30),(0,255,255),(100,100,100),(50,50,50),cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill_color_demo",copyimage)

def fill_binary():
    image = np.zeros((400,400,3),np.uint8)
    image[100:300,100:300,:]=255
    cv.imshow("fill_binary",image)

    mask=np.ones((402,402,1),np.unit8)
    mask[100:300,100:300,:]= 0
    cv.floodFill(image,mask,(200,200),(100,2,255),cv.FLOODFILL_MASK_ONLY)
    cv.imshow("filled binary",image)
#ROI(Region of interest)  也就是找出感兴趣的那个为主

print("--------------------Hi, Python------------------------------")
src = cv.imread("D:\\Onedrive\\Bilder\\chen.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# 创建窗口的namedWindow default parameter为WINDOW_AUTOSIZE。窗口大小会自动调整以适应所显示的图像，但是不能更改大小
"""""
cv.imshow("input image",src)
getpart = src[200:300,100:500]# 似乎这个感兴趣的都是人为手动的操作
src[200:300,100:500] = cv.cvtColor(cv.cvtColor(getpart,cv.COLOR_BGR2GRAY),cv.COLOR_GRAY2BGR)
cv.imshow("recover",src)
"""""
fill_color_demo(src)
cv.waitKey(0) # 无限制等待用户的按键事件
cv.destroyAllWindows()

# 导入后，图片就会变成变成numpy