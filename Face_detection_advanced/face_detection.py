import cv2, sys, numpy, os

size = 4
haar_file = "C:/Users/dylan/OneDrive/Desktop/Dev/Jetlearn/OpenCV/haarcascade_frontalface_default.xml"
datasets = "C:/Users/dylan/OneDrive/Desktop/Dev/Jetlearn/OpenCV/datasets"

#part 1: create fisher recogniser
print("recognising face, please be in sufficient light...")

#create a list of images under a list of corisponding names
(images, labels, names, ID) = ([], [], {}, 0)

for (sub_dirs, dirs, files) in os.walk(datasets):
    for sub_dir in dirs:
        names[ID] = sub_dir
        subject_path = os.path.join(datasets, sub_dir)
        for file_name in os.listdir(subject_path):
            path = subject_path + "/" + file_name
            label = ID
            images.append(cv2.imread(path, 0))
            labels.append(int(label))

        ID += 1

(WIDTH, HEIGHT) = (130, 100)

#create a numpy array from the two lists above
# (images, labels) = [numpy.array(lis) for lis in (images, labels)]
# images = numpy.array(images)
# labels = numpy.array(labels)
# numpy.array([images, labels])
for i, img in enumerate(images):
    print(f"Image {i}: type={type(img)}, shape={getattr(img, 'shape', 'N/A')}")

images = numpy.array(images, dtype=object)
labels = numpy.array(labels)

#open CV trains the model from the images
model = cv2.face.LBPHFaceRecognizer_create()
model.train(images, labels)

#part 2: use fisher recogniser on camera stream
face_casade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(1)
while True:
    (_, im) = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_casade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x+w, y+h), (255, 0, 0), 2)
        face = gray[y:y+h, x:x+w]
        face_resize = cv2.resize(face, (WIDTH, HEIGHT))
        #try to recognise the faces
        prediction = model.predict(face_resize)
        cv2.rectangle(im, (x, y), (x+w, y+h), (0, 255, 0), 3)

        if prediction[1] > 20:
            cv2.putText(im, '% s - %.0f' %
            (names[prediction[0]], prediction[1]), (x-10, y-10),
            cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
        else:
            cv2.putText(im, 'not recognized',
            (x-10, y-10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0))
            
    cv2.imshow('OpenCV', im)

    key = cv2.waitKey(10)
    if key == 27:
        break

