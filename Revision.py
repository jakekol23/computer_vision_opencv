import numpy as np
import cv2

def read_image(img_path, img_name):

    complete_path = img_path + img_name
    img = cv2.imread("images/", "image_2.jpg")
    
    while True:
        
        cv2.imshow("food window", img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            
            break
    cv2.destroyAllWindows()


read_image()

 


