import cv2

img = cv2.imread("giadinh.jpg")

px = img[0][0]

print(px)

cv2.waitKey(0)
cv2.destroyAllWindows()