import cv2 

img = cv2.imread("images/image_1.jpg")
img2 = cv2.imread("images/image_3.jpg")

while True:
    cv2.imshow("Food window", img)
    cv2.imshow("Snack window", img2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #when everything done, release the capture


cv2.destroyAllWindows()



def read_image():
    img_path = cv2.imread("images/", "image_3")

    img_name = cv2.imshow("food window", img_path)


while True:
    cv2.imshow("food window", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()