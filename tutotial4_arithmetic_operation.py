import cv2 as cv
import numpy as np

#addition
def add_demo(image1,image2):
    result =cv.add(image1,image2)
    cv.imshow("result1",result)

def sub_demo(image1,image2):
    result =cv.subtract(image1,image2)
    cv.imshow("result2",result)

def div_demo(image1,image2):
    result =cv.divide(image1,image2)
    cv.imshow("result3",result)

def mul_demo(image1,image2):
    result =cv.multiply(image1,image2)
    cv.imshow("result4",result)

def others(image1,image2):
    #mean1 = cv.mean(image1)
    #mean2 = cv.mean(image2)

    mean1,dev1 = cv.meanStdDev(image1)
    mean2,dev2 = cv.meanStdDev(image2)

    print(image1.shape[:2])
    print(image1.shape[:1])
    print(image1.shape[:0])
    #print(mean1)
    #print(mean2)
    #print(dev1)
    #print(dev2)

#逻辑运算
def logic_demo(image1,image2):
    result1 = cv.bitwise_and(image1,image2)
    result2 = cv.bitwise_or(image1, image2)
    result3 = cv.bitwise_not(image1)

    cv.imshow("result1",result1)
    cv.imshow("result2", result2)
    cv.imshow("result3", result3)

def contrast_brightness_demo(image,c,b):
    h,w,ch = image.shape
    blank = np.zeros([h,w,ch],image.dtype)
    # 假设图片中的对比度是2和8，分别乘以百分之50就是1和4， 如果乘以百分之百就是2和8 ，如果乘以四分之一，那就是0，5和2 如此来降低对比度
    dst = cv.addWeighted(image,c,blank,1-c,b)
    cv.imshow("demo",dst)

print("--------------------Hi, Python------------------------------")
src1 = cv.imread("D:\\tools\\opencv\\opencv\\sources\\samples\\data\\LinuxLogo.jpg")
src2 = cv.imread("D:\\tools\\opencv\\opencv\\sources\\samples\\data\\WindowsLogo.jpg")
cv.namedWindow("input image1", cv.WINDOW_AUTOSIZE)
# 创建窗口的namedWindow default parameter为WINDOW_AUTOSIZE。窗口大小会自动调整以适应所显示的图像，但是不能更改大小
cv.imshow("input image1",src1)
print(src1.shape)
cv.namedWindow("input image2", cv.WINDOW_AUTOSIZE)
# 创建窗口的namedWindow default parameter为WINDOW_AUTOSIZE。窗口大小会自动调整以适应所显示的图像，但是不能更改大小
cv.imshow("input image2",src2)
print(src2.shape)
#add_demo(src1,src2)
#sub_demo(src1,src2)
#div_demo(src1,src2)
#mul_demo(src1,src2)
#others(src1,src2)
logic_demo(src1,src2)
cv.waitKey(0) # 无限制等待用户的按键事件
cv.destroyAllWindows()