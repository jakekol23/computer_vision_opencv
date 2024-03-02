#!/usr/bin/python3

import cv2 as cv
import numpy as numpy

cap = cv.VideoCapture(0)#o means PC webcam and 2 for a USB cam

while True:

    #Capture frame.by.frame
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('frame', gray)    
    cv.imshow('frame2', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    

cap.release()
cv.destroyAllWindows()




