import cv2
import  matplotlib.pyplot as plt


print(cv2.__version__)
img=cv2.imread('3.jpg',cv2.IMREAD_COLOR)
print(img.shape)
cv2.imshow('Image',img)
cropped=img[250:775,310:885]
cv2.imshow('Cropped Image',cropped)
cv2.waitKey(0)
cv2.destroyAllWindows
