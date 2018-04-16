import numpy as np
import cv2

# capture video
cap = cv2.VideoCapture('./media/test1.mp4')
out = None


#descripe a loop
#read video frame by frame
frame_num = 500
while frame_num:
    frame_num -= 1
    ret, img = cap.read()
    #flip for truning(fliping) frames of video
    img2 = cv2.flip(img, -1)
    if ret == 0:
        break
    if out is None:
        [h, w] = img2.shape[:2]
        out = cv2.VideoWriter('./media/rotate.avi', 0, 25.0, (w,h))
    out.write(img2)
cap.release()
out.release()


