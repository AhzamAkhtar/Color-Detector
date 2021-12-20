#pip intall opencv-contrib-python
import cv2 as cv
import numpy as np
import pyautogui
capture=cv.VideoCapture(0)
prev_y=0
prev_x=0
while True:
    ret,frame=capture.read()
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    mask=cv.inRange(hsv,(36,25,25),(70,255,255))
    contours,h=cv.findContours(mask,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    for c in contours:
        area=cv.contourArea(c)
        if area>300:
            #print(area)
            # TO REDUCE SMALL NOISE/CONTOURS
            x,y,w,h=cv.boundingRect(c)
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            if y<prev_y:

                # by pressing space inst,tiktok scroll down
                #pyautogui.press("space")
                pyautogui.press("down")
            prev_y=y
            '''if x<prev_x:
                pyautogui.press("up")
            prev_x=x'''
            #cv.drawContours(frame,c, -1, (0, 255, 0), 2)
    #cv.drawContours(frame,contours,-1,(0,255,0),2)
    cv.imshow("frame",frame)
    #cv.imshow("yellow",mask)
    if cv.waitKey(30)==ord("q"):
        break
capture.release()
cv.destroyAllWindows()

'''
import cv2
import numpy as np

## Read
img = cv2.imread("sunflower.jpg")

## convert to hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

## mask of green (36,25,25) ~ (86, 255,255)
# mask = cv2.inRange(hsv, (36, 25, 25), (86, 255,255))
mask = cv2.inRange(hsv, (36, 25, 25), (70, 255,255))

## slice the green
imask = mask>0
green = np.zeros_like(img, np.uint8)
green[imask] = img[imask]

## save 
cv2.imwrite("green.png", green)
'''