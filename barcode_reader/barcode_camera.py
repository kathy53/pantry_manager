import cv2
from pyzbar import pyzbar 

url = "http://192.168.178.248:8080/video"
cp = cv2.VideoCapture(self.url)

while True:
    _, frame = cp.read()  #_ = boolean value is or not video
    frame = cv2.resize(frame, (0,0), fx=0.50, fy=0.50)
    cv2.putText(frame, "Press q to close camera",, (10,10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255,100),1)

    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        (x,y,w,h) = barcode.rect
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1)
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        text = f"Barcode: {barcodeData} Type: {barcodeType}"
        cv2.putText(frame, text, (x,y-10, cv2FONT_HERSHEY_SIMPLEX, 0.5, (0, 255,100),1))
    cv2.imshow("Barcode Scanner", frame)
    if cv2.waitKey(1) == ord(q):
        break
cp.release()
cv2.destroyAllWindows()
