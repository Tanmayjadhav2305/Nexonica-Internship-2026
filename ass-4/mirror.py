import cv2

img = cv2.imread("image.jpeg")
img2 = img.copy()

if img is None:
    print("Image not found")
else:
    cv2.imshow("Original", img)

    h, w, c = img.shape

    for y in range(h):
        for x in range(w):
            img2[y][w - 1 - x] = img[y][x]

    cv2.imshow("Mirror Image (Horizontal)", img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
