import cv2 
from pyzbar.pyzbar import decode

img = cv2.imread("crackets.jpg")    #reading the image
print(decode(img))                  #find the barcode and decode each barcode
