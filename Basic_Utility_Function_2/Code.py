import cv2
import numpy as np

#grayscaling of color image
image = cv2.imread("Images/Blue_sky_bg.png")

cv2.imshow("Original Image", image)

#cvtcolor function is going to grayscale the image
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscaled image", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#using average pixels to grayscale an image
image = cv2.imread("Images/Blue_sky_bg.png")

cv2.imshow("Original Image", image)

(row, col) = image.shape[0:2]
for i in range(row):
    for j in range(col):
        #find the average of BGR values
        image[i, j] = sum(image[i, j]) * 0.33

cv2.imshow("Grayscale image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#rotating an image
image = cv2.imread("Images/Blue_sky_bg.png")

(row, col) = image.shape[:2]
#get rotation metrix 2D, this creates a metrix need for transformation
m = cv2.getRotationMatrix2D((col/2, row/2), 180, 1)
res = cv2.warpAffine(image, m, (col, row))
cv2.imwrite("Result.jpg", res)

#edge detection in an image
image = cv2.imread("Images/Blue_sky_bg.png")
edges = cv2.Canny(image, 100, 200)
cv2.imwrite("Edges.jpg", edges)

#converting image from one color frame to another
image = cv2.imread("Images/Blue_sky_bg.png")
hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Image", hsv_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
