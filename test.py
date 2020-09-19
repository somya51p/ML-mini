import cv2

img = cv2.imread("sign-up.jpg")
print(img.shape)

imgResize = cv2.resize(img,(500,500))
imgCropped = img[100:200,200:500]

cv2.imshow("Image",img)
cv2.imshow("Image resize",imgResize)
#cv2.imshow("Image cropped",imgCropped)

cv2.waitKey(0)