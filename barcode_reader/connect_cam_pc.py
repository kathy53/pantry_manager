import cv2
#url = "http://192.168.178.248:8080/shot.jpg" 
url = "http://192.168.178.248:8080/video"
capture = cv2.VideoCapture(url)

while(True):
    _, frame = capture.read()  #_ = boolean value is or not video
    frame = cv2.resize(frame, (0,0), fx=0.50, fy = 0.50)
    cv2.imshow("live_stream", frame)

    if cv2.waitKey(1) == ord("q"):  #1-press
                                    #q-letter q in the keyboard
        break                            
capture.release()
cv2.destroyAllWindows()
