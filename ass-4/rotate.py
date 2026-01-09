import cv2
import numpy as np

img = cv2.imread("image.jpeg")

if img is None:
    print("Image not found")
else:
    cv2.imshow("Original", img)

    h, w, c = img.shape

    # create new image with swapped width & height
    img2 = np.zeros((w, h, c), dtype=np.uint8)

    for y in range(h):
        for x in range(w):
            img2[x][h - 1 - y] = img[y][x]

    cv2.imshow("Rotated 90 Clockwise", img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
