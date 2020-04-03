import cv2 as cv
import numpy as np

# numpy 其实就是对矩阵运算的一个库
import numpy as np
"""""
a = np.array([[4, 3, 5], [1, 2, 1]], np.uint32)# 对于图像来说,这是最基本的要求
a.fill(9)
print(a)
"""""

#b = np.sort(a, axis=1)
#print b
#b
#a.sort(axis=1)
#print a
a = np.array([4, 3, 1, 2]) #Returns the indices that would sort an array.
j = np.argsort(a)
print (j)
print (a[j])


c = np.ones([200,200,3],np.uint8)
d = np.zeros([200,200,3],np.uint8)


def get_imgae(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("width: %s, height:%s, channels: %s"%(width, height, channels))
    for i in range(height):
        for j in range(width):
            for k in range(channels):
                image[i,j,k] = 255 - image[i,j,k]
    cv.imshow("new image", image)


def create_image():
    img = np.zeros((400,400,3),np.uint8)
    img[:,:,0] = np.ones((400,400))*255#BGR
    cv.imshow("new image",img)

def reverse(image):
    img =np.bitwise_not(image)
    cv.imshow("new image", img)

a = np.floor(10*np.random.random((4,2,3)))# 从矩阵的角度来说，random的第一个数字就是多维度的
b = np.floor(10*np.random.random((2,2)))
print(a)
print ('---')
print(b)
print ('---')


src = cv.imread("D:\\Onedrive\\Bilder\\chen.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# 创建窗口的namedWindow default parameter为WINDOW_AUTOSIZE。窗口大小会自动调整以适应所显示的图像，但是不能更改大小
cv.imshow("input image",src)
tickcount1 = cv.getTickCount()
get_imgae(src)
tickcount2 = cv.getTickCount()
tickcount = tickcount2 - tickcount1
print("the time %s ms" %((tickcount/cv.getTickFrequency())*1000) )# 测时间
cv.waitKey(0) # 无限制等待用户的按键事件
cv.destroyAllWindows()

np.reshape

# 导入后，图片就会变成变成numpy