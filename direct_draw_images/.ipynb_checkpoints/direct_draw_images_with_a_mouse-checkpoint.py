import cv2
import numpy as np

#define the parameters for the function
#these are mostly being filled by the call bacl
def draw_circle(event, x,y,flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        #pass the image,
        # x,y are coming from the call back
        #100 = redius
        #(0,255,0) color
        # -1 = inverted ( fill inside the circle )
        cv2.circle(img,(x,y),100,(0,255,0),-1)

#link the image to event call back use the window name
#in this sample is 'emi_image'
cv2.namedWindow(winname='emi_image')
cv2.setMouseCallback('emi_image', draw_circle)

#show image
shape = (512, 512, 3)
img = np.zeros(shape, np.int8)

while True:
    cv2.imshow('emi_image', img)
    #wait 20 milliseconds to see if 'esc has been pressed
    if cv2.waitKey(20) & 0xFF == 27:
        break

#destroy all cv2 image resources
cv2.destroyAllWindows()