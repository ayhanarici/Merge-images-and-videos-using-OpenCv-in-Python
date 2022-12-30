import cv2
import time
import random
background_image = cv2.imread("istanbul.jpg")
#Video Source = https://www.youtube.com/watch?v=CNjggrxUQ78
cap = cv2.VideoCapture("fire.mp4")
fps= int(cap.get(cv2.CAP_PROP_FPS))
background_image = cv2.resize(background_image, (1280,720))
x=150
y=700
while cap.isOpened():
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.resize(frame, (1280, 720))
        cv2.putText(frame, "Happy New Year",(x, y), cv2.FONT_HERSHEY_TRIPLEX, 2.0, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        cv2.putText(frame, "2023",(x+650, y), cv2.FONT_HERSHEY_TRIPLEX, 4.0, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        output_image = cv2.add(frame, background_image, frame)
        cv2.imshow("Happy New Year", output_image)
        output_image = None
    else:
        break
    time.sleep(1/fps)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
