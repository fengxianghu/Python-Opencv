import cv2 as cv
import numpy as np

def get_image_info(image):
    print(image.size)
    print(image.shape)
    print(image.dtype)
    print(type(image))
    pixel_data = np.array(image)
    print(pixel_data)

def video_demo():
    capture = cv.VideoCapture(0)# 0 或者是路径
    while(True):
        ret,frame = capture.read()
        frame = cv.flip(frame,1)
        cv.imshow("video",frame)
        c = cv.waitKey(50) # 每 50s 等待一次键盘输入
        if c == 27:
            break


print("--------------------Hi, Python------------------------------")
src = cv.imread("D:\\Onedrive\\Bilder\\chen.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# 创建窗口的namedWindow default parameter为WINDOW_AUTOSIZE。窗口大小会自动调整以适应所显示的图像，但是不能更改大小
cv.imshow("input image",src)
get_image_info(src)
video_demo()
cv.waitKey(0) # 无限制等待用户的按键事件
cv.destroyAllWindows()

# 导入后，图片就会变成变成numpy
