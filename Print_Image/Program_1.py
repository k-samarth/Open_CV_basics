#importing
import cv2
import numpy as np
import matplotlib.pyplot as plt

#assign image to a variable
img = cv2.imread("res/lena.jpg", -1)

#Saving image
cv2.imwrite("result/lena_unchanged.jpg",img)

#Displaying image
cv2.imshow("image",img)
#Wait till a key is pressed
cv2.waitKey(0)
#Close all created image windows
cv2.destroyAllWindows()
