import cv2
import matplotlib.pyplot
import numpy as np 

img = np.zeros((250, 500, 3))

img = cv2.line(img, (400, 100),(100,200),(0,0,255), 1)

img = cv2.rectangle(img, (50,100),(450,150),(255,0,0), -1)

img = cv2.circle(img, (150,150), 50,(0,255,0),-1)

font = cv2.FONT_HERSHEY_SIMPLEX
string = "Our shapes"
img = cv2.putText(img, string, (50,150),font, 1, (255,255,255), 5)

pts = np.array([[100,100],[150,150],[250,200]],np.int32)
img = cv2.polylines(img, [pts],True,(0,255,255),5)

cv2.imwrite("result/shapes.jpg",img)

cv2.imshow("Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
