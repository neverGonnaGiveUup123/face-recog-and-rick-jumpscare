import cv2
import time

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    time.sleep(1)
    cv2.imshow("capturing",frame)
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    key = cv2.waitKey(100)
    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows()