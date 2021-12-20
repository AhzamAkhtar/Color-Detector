#pip intall opencv-contrib-python
import cv2 as cv
import pyautogui

capture=cv.VideoCapture(0)
harr_cascade=cv.CascadeClassifier("haar_face.xml")
x_init=0
y_init=0
while True:
    ret,frames=capture.read()
    gray=cv.cvtColor(frames,cv.COLOR_BGR2GRAY)
    face=harr_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
    for x,y,w,h in face:
        cv.rectangle(frames,(x,y),(x+w,y+h),(0,255,0),thickness=3)
        if y<y_init:
            pyautogui.press("down")
        y_init=y
        '''if x<x_init:
            pyautogui.press("up")
        x_init=x'''
    cv.imshow("face",frames)
    if cv.waitKey(30)==ord("q"):
        break
cv.release()
cv.destroyAllWindows()