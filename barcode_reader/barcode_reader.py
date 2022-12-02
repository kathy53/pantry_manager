import cv2 
from pyzbar.pyzbar import decode

img = cv2.imread("crackets.jpg")
print(decode(img))