import cv2
class Streaming_from_mobile:
    def streaming(self, url):
        self.url = url
        cp = cv2.VideoCapture(self.url)
        while True:
            _, frame = cp.read()  #_ = boolean value is or not video
            #frame = cv2.resize(frame, (0,0), fx=0.50, fy=0.50)
            cv2.imshow("live_stream", frame)
            if cv2.waitKey(1) == ord("q"):  #1-press
                                            #q-letter q in the keyboard
                break                            
        cp.release()
        cv2.destroyAllWindows()

cam = Streaming_from_mobile()

#url = "http://192.168.178.248:8080/shot.jpg"
url = "http://192.168.178.248:8080/video"

cam.streaming(url)