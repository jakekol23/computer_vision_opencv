import cv2 as cv
import numpy as np

RED = (0, 0, 255)
YELLOW = (0, 255, 255)

p0, p1, p2 =(10, 10), (300, 300), (400, 10)

img = img = np.zeros((100, 500, 3), np.uint8)

cv.line(img, p0, p1, RED, 2)
cv.line(img, p1, p2, YELLOW, 5)

cv.imshow('RGB',img)

gray_img = np.zeros((100, 500), np.uint8)

cv.line(gray_img, p0, p1)