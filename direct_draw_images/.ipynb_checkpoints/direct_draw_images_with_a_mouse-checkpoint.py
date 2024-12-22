import cv2
import numpy as np

#add image
def draw_circle(event, x,y,flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,255,0),-1)


cv2.namedWindow(winname='emi_image')
cv2.setMouseCallback('emi_image', draw_circle)

#show image
shape = (512, 512, 3)
img = np.zeros(shape, np.int8)

while True:
    cv2.imshow('emi_image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()