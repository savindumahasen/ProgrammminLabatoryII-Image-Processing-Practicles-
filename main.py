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
