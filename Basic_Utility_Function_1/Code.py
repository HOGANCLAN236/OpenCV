import cv2, numpy as np

#load 2 images
img1 = cv2.imread("Images/water_bg.jpg", cv2.IMREAD_COLOR)
img2 = cv2.imread("Images/Blue_sky_bg.png", cv2.IMREAD_COLOR)

weight_sum = cv2.addWeighted(img1, 0.2, img2, 0.8, 0)
cv2.imshow("Display Image", weight_sum)
cv2.waitKey(0)
cv2.destroyAllWindows()

#resizing image

img1resize = cv2.imread("Images/water_bg.jpg", cv2.IMREAD_COLOR)
cv2.imshow("original", img1resize)

resized = cv2.resize(img1resize, (400, 400))
cv2.imshow("resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

#blurring of an image
#bluring out of three types: gaussin blur, median blur, bilateral blur

blur1 = cv2.imread("Images/Blue_sky_bg.png", 1)
cv2.imshow("Original Image", blur1)

#gaussin blur - mostly used in machine learning pre-processing steps
gaussin = cv2.GaussianBlur(blur1, (7, 7), 0)
cv2.imshow("Gaussian Blur", gaussin)
cv2.waitKey(0)
cv2.destroyAllWindows()

blur1 = cv2.imread("Images/Blue_sky_bg.png", 1)
cv2.imshow("Original Image", blur1)

#median blur - Used in digital processing but it proserves edges and removes noise
median = cv2.medianBlur(blur1, 5)
cv2.imshow("Median Blur", median)
cv2.waitKey(0)
cv2.destroyAllWindows()

blur1 = cv2.imread("Images/Blue_sky_bg.png", 1)
cv2.imshow("Original Image", blur1)

#bilateral blur - Only sharp edges are presevered here
bilateral = cv2.bilateralFilter(blur1, 9, 75, 45)
cv2.imshow("Bilateral Blur", bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()

#bordering an image
border = cv2.imread("Images/Blue_sky_bg.png", 1)
borderedImage = cv2.copyMakeBorder(border, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value=1)
cv2.imshow("Original Image", borderedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Reflective border around an image
border = cv2.imread("Images/Blue_sky_bg.png", 1)
borderedImage = cv2.copyMakeBorder(border, 200, 200, 200, 200, cv2.BORDER_REFLECT, value=1)
cv2.imshow("Original Image", borderedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
