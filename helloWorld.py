# Open an image

# import cv2 library
import cv2

# read giadinh.jpg image and assign to img variable
img = cv2.imread("giadinh.jpg")

# Open the image
# giadinh.jpg will be displayed as file title | img as a reference
cv2.imshow("giadinh.jpg", img) 

# Wait until I turn it off
cv2.waitKey(0)
#destroy all windows when I turn the image off
cv2.destroyAllWindows()
