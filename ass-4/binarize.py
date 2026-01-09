import cv2

img = cv2.imread("image.jpeg")
img2 = img.copy()

if img is None:
    print("Image not found. Check filename or path.")
else:
    cv2.imshow("Original Image", img)

    h, w, c = img.shape
    print(w, h, c)

    for y in range(h):
        for x in range(w):
            b, g, r = img[y][x]
            avg = (int(b) + int(g) + int(r)) // 3

            if avg > 127:
                img2[y][x] = (255, 255, 255)
            else:
                img2[y][x] = (0, 0, 0)

    cv2.imshow("Binarized Image", img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
