import cv2

img = cv2.imread('rick.jpg',1)

resized = cv2.resize(img,(int(img.shape[1]*4),int(img.shape[0]*4)))

cv2.imshow("New-image",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()