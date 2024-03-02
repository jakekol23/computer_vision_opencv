# import the openCV.library
import cv2 as cv
import numpy as np


zeros_3d = np.zeros((1200, 1200, 3)) # creates a black image

zeros_3d[:300, :255,:] = 100



# Create a 3x3 image array with three channels (RBG)
image_array = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]],
                       [[255, 255, 0], [255, 0, 255], [0, 255, 255]],
                       [[128, 128, 128], [64, 64, 64], [192, 192, 192]]], dtype=np.uint8)

#Read the image from where it is located on the PC
img = cv.imread('images/image_2.jpg')
image_array = np.array(img)
shape = image_array.shape
print(shape)
img[:100,:100,:] = 100


#start a while loop that continues to show the image on the windows
while True:
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('food window',zeros_3d)
    if cv .waitKey(1) & 0xFF == ord('a'):
        break


cv.destroyAllWindows()

'''
Numpy array

In the slicing image_array[1:, 1:, 1:], each colon (:) represents a range of indices along a particular
dimension of the array. In a 3D numpy array representing an image with dimensions (height, width, channels),
the slicing corresponds to:

1::This indicates that we are selecting elementsstarting from index 1 (the second element) along the first dimension
(height) This meanswe are excluding the first row of the image.

1::Similarly, this indicates that we are selecting elementsstarting from index 1 (the second element) along the second dimension
(width), This means we are excluding the first column of the image.

1::Finally, This indicates that we are selecting elements starting from index 1 (the second element) along the third
dimension (channels). This means we are excluding the first channel of the image.
So, subimage will contain a cropped version of image_array that excludes the first row, first column,
and first channel. It represents a sub image of the original image with dimensions (height - 1, width - 1, channels - 1).


'''   