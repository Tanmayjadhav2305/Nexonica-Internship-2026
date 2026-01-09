#pip install opencv-python

import cv2

img = cv2.imread("image.jpeg")   # image must be in same folder
img2=img.copy()

if img is None:
    print("Image not found. Check filename or path.")
else:
    cv2.imshow("Image", img)
    #get height width channel of image

    h,w,c=img.shape
    print(w,h,c)
    for y in range(h):
        for x in range(w):
            b,g,r=img[y][x]
            avg=(int(b)+int(g)+int(r))/3
            
            #img.putpixel((x,y),(255,0,0))
            img2[y][x]=(avg,avg,avg)
    cv2.imshow("imagegray",img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()