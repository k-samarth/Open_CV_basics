import cv2
import matplotlib.pyplot
import numpy as np 

img = np.zeros((250, 500, 3))

img = cv2.rectangle(img, (0, 94),(62, 156),(255,0,0), -1)

img = cv2.line(img, (69,125),(431,125),(0,0,255),5)

img = cv2.circle(img, (469,125),31,(0,255,0),-1)

pts = np.array([[0,0],[500,250],[0,250],[500,0]],np.int32)
img = cv2.polylines(img, [pts],True,(0,255,255),5)

font = cv2.FONT_HERSHEY_SIMPLEX
string = "Code By Samarth"
img = cv2.putText(img, string, (180,200),font, 0.5, (255,255,255), 1)

cv2.imwrite("result/code_by_samarth.jpg",img)

cv2.imshow("Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
