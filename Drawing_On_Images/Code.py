import cv2, numpy as np

image = "Images/Blue_sky_bg.png"

#---------------------------------------

img = cv2.imread(image)

#drawing a line on the image
#Start Co-ordinated will represent the top left corner and the end Co-ordinated represents the bottom right corner

Start_point = (0, 0)
End_point = (450, 450)
color = (255, 0, 0)
thickness = 9

line = cv2.line(img, Start_point, End_point, color, thickness)


cv2.imshow("Image", line)
cv2.waitKey(0)
cv2.destroyAllWindows()

#---------------------------------------

img = cv2.imread(image)

#drawing a rectangle on the image
#Start Co-ordinated will represent the top left corner and the end Co-ordinated represents the bottom right corner

Start_point = (0, 0)
End_point = (450, 250)
color = (0, 0, 255)
thickness = 3

rect = cv2.rectangle(img, Start_point, End_point, color, thickness)

cv2.imshow("Image", rect)
cv2.waitKey(0)
cv2.destroyAllWindows()

#---------------------------------------

img = cv2.imread(image)

#drawing a filled rectangle on the image
#Start Co-ordinated will represent the top left corner and the end Co-ordinated represents the bottom right corner

Start_point = (100, 150)
End_point = (700, 450)
color = (0, 0, 255)
thickness = -1

rect = cv2.rectangle(img, Start_point, End_point, color, thickness)

cv2.imshow("Image", rect)
cv2.waitKey(0)
cv2.destroyAllWindows()

#---------------------------------------

img = cv2.imread(image)

#drawing a filled circle on the image
#Start Co-ordinated will represent the top left corner and the end Co-ordinated represents the bottom right corner

window_name = "Circle Image"
center_coords = (400, 300)
radius = 20
color = (0, 0, 255)
color_2 = (255, 0, 255)
thickness = 5
radius_2 = radius - thickness
thickness_2 = -1

circle = cv2.circle(img, center_coords, radius, color, thickness)
circle2 = cv2.circle(img, center_coords, radius_2, color_2, thickness_2)

cv2.imshow(window_name, circle)
cv2.imshow(window_name, circle2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#---------------------------------------

#drawing text on an image
img = cv2.imread(image)

#font for setting up the text specifications
font = cv2.FONT_HERSHEY_COMPLEX
origin = (100, 200)
font_scale = 1
color = (0, 0, 255)
thickness = 2

text_img = cv2.putText(img, "This is my first text with OpenCV!!!!", origin, font, font_scale, color, thickness, cv2.LINE_AA)

cv2.imshow("Text", text_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#---------------------------------------

#drawing elipse on image
img = np.zeros((500, 500, 3), dtype=np.uint8)

#drawing an elipse

center_coords = (250, 250)
color = (0, 0, 255)
thickness = 3
axis = (150, 100)
angle = 45
start_angle = 0
end_angle = 360

elipse = cv2.ellipse(img, center_coords, axis, angle, start_angle, end_angle, color, thickness)

cv2.imshow("ellipse", elipse)
cv2.waitKey(0)
cv2.destroyAllWindows()

#---------------------------------------

#drawing polylines
image = np.zeros((500, 500, 3), dtype=np.uint8)
points = np.array([[100, 300], [200, 150], [400, 200], [400, 350], [150, 400], [300, 250]], np.int32)
points = points.reshape((-1, 1, 2))  # Reshape for OpenCV compatibility
isClosed = True  # True means it will draw a closed shape

cv2.polylines(image, [points], isClosed, (255, 0, 0), thickness=2)  # Blue color

# Display the Image
cv2.imshow('Polylines', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
