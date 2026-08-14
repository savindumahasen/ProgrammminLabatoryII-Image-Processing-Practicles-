import cv2
import  matplotlib.pyplot as plt


print(cv2.__version__)
img=cv2.imread('3.jpg',cv2.IMREAD_COLOR)
print(img.shape)
cv2.imshow('Image',img)
cropped=img[250:775,310:885]
cv2.imshow('Cropped Image',cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

## resize the image
img_resize= cv2.resize(img,(800,900))
## convert the BGR into  RGB 
img_RGB=cv2.cvtColor(img_resize,cv2.COLOR_BGR2RGB)
# Plot the image using   matplotlib library
plt.subplot(1,2,1)
plt.imshow(img_RGB)

plt.subplot(1,2,2)
plt.imshow(img_RGB)
plt.show()

kali=cv2.imread('download.jpg',cv2.IMREAD_COLOR)
## image resize
kali_resize=cv2.resize(kali,(1000,1200))
kali_RGB=cv2.cvtColor(kali_resize,cv2.COLOR_BGR2RGB)

print(kali_resize.shape)
plt.subplot(2,2,3)
plt.imshow(img_RGB)

plt.subplot(2,2,2)
plt.imshow(kali_RGB)
plt.show()

## Split the image into  three channels
img=cv2.imread(r'3.jpg',cv2.IMREAD_COLOR)
b,g,r=cv2.split(img)
b[:]=0   # or [:,:]
merged_img=cv2.merge((b,g,r))
cv2.imshow('Merged Image',merged_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

## convert the bgr value into  rgb 
merged_img_rgb=cv2.cvtColor(merged_img,cv2.COLOR_BGR2RGB)
## plot the merged  blue color removed image using matplot lib
plt.subplot(1,2,1)
plt.imshow(merged_img_rgb)
plt.show()


