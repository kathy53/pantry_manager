#I am not able to acces the camera


import cv2                 #read images, camera, and video
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(-1)
cap.set(3, 640)            #3-width
cap.set(4, 480)            #4-height
camera = True

while camera == True:
    success, frame = cap.read()
    
    for code in decode(frame):
        print(code.type)
        print(code.data.decode("utf-8"))
    cv2.imshow("Testing-code-scan", frame)
    cv2.waitKey(1)