import cv2
import numpy as np

def exit(a):
    pass
capture = cv2.VideoCapture(0)

cv2.namedWindow("Trackbars")
cv2.createTrackbar("h_min","Trackbars",0,179,exit)
cv2.createTrackbar("h_max","Trackbars",179,179,exit)
cv2.createTrackbar("s_min","Trackbars",0,255,exit)
cv2.createTrackbar("s_max","Trackbars",255,255,exit)
cv2.createTrackbar("v_min","Trackbars",1,255,exit)
cv2.createTrackbar("v_max","Trackbars",74,255,exit)
def getcolor(img):
    hmin = cv2.getTrackbarPos("h_min","Trackbars")
    hmax = cv2.getTrackbarPos("h_max","Trackbars")
    smin = cv2.getTrackbarPos("s_min","Trackbars")
    smax = cv2.getTrackbarPos("s_max","Trackbars")
    vmin = cv2.getTrackbarPos("v_min","Trackbars")
    vmax = cv2.getTrackbarPos("v_max","Trackbars")
    upper = np.array([hmax,smax,vmax])
    lower = np.array([hmin,smin,vmin])
    mask = cv2.inRange(hue,lower,upper)
    return mask


while True:
    success,initial = capture.read()
    cv2.waitKey(1000)
    cv2.imshow("replace",initial)
    if(success):
        break
while True:
    success2, img = capture.read()

    hue = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask = getcolor(hue)
    inv_mask = 255 - mask
    black = cv2.bitwise_and(img,img,mask=inv_mask)
    white = cv2.bitwise_and(initial,initial,mask=mask)
    # cv2.imshow("first", img);
    # cv2.imshow("mask",mask)
    # cv2.imshow("Black",black)
    # cv2.imshow("white",white)
    finalresult = cv2.bitwise_or(black,white)
    cv2.imshow("FinalResult",finalresult)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
