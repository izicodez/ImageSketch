from tkinter import Scale
import cv2
img = cv2.imread("download.jpg")

gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

inv_gray_image = 255-gray_image

blur_inv_gray_image = cv2.GaussianBlur(inv_gray_image,(19,19),0)

inv_blur_imaage = 255-blur_inv_gray_image

sketch = cv2.divide(gray_image,inv_blur_imaage,scale=256.0)

cv2.imshow("OG image", img)

cv2.imshow("Sketch", sketch)

cv2.waitKey(0)