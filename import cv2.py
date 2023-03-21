import cv2
videoCaptureObject = cv2.VideoCapture(0)

while(True):
    ret,frame = videoCaptureObject.read()
    cv2.imwrite("png1.jpg",frame)
    result = False
videoCaptureObject.release()
cv2.destroyAllWindows()
