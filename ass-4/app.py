#pip install opencv-python

import cv2

img = cv2.imread("image.jpeg")   # image must be in same folder

if img is None:
    print("Image not found. Check filename or path.")
else:
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()