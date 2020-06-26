#importing opencv2
import cv2

#variable to read video
cap = cv2.VideoCapture('res/30_10fps.avi')

#fourcc
fcc = cv2.VideoWriter_fourcc('X','V', 'I', 'D')

#saving the video
output = cv2.VideoWriter('result/30_30fps_hsv.mp4', fcc, 30.0, (400,200))

while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow("Frame",frame)
    
    output.write(frame)

    if cv2.waitKey(1) == 27:
        break
cap.release()
output.release()
