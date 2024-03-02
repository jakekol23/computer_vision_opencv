import cv2 as cv
import numpy as np


zeros_3d = np.zeros((1200, 1200, 3)) # creates a black image

zeros_3d[150:,300:,1:] = 200

# Create a 3x3 image array with three channels (RBG)
image_array = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]],
                       [[255, 255, 0], [255, 0, 255], [0, 255, 255]],
                       [[128, 128, 128], [64, 64, 64], [192, 192, 192]]], dtype=np.uint8)

#Read the image from where it is located on the PC
img = cv.imread('images/image_2.jpg')
img_array = np.array(img)
shape = image_array.shape
print(shape)
img[100, :200,:] = 100
sub = img[:100, :300]
img[100:200, 200:500] = sub


#start a while loop that continues to show the image on the windows
while True:
    image_array = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('food window',img)
    if cv .waitKey(1) & 0xFF == ord('a'):
        break

cv.imwrite("my image.jpg",img)
cv.destroyAllWindows()
