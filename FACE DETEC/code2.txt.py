import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier(r'FACE DETEC/picture1.jpg

det
face_extractor(img):

gray = cv2.cvtColor(img, cv2.COLOR_BGRZGRAY)
faces = face_classifier.detectMultiScale(gray, 1.3, 5)

if faces is ():
    return None
for (x, y, w, h) in faces:cropped_face = img[y:y + h, x:x + w]
return cropped_face
cap = cv2.VideoCapture(0)
count0
while True:
    ret, frame = cap.read()
if face extractor (frame) is not None: count += 1

face = cv2.resize(face
extractor(frame), (200, 200))
face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

file
name_path = r'FACE DETEC/picture1.jpg’.jp cv2.imwrite (file_name_path, FACE DETEC)
cv2.putText(face, str(count), (50, 50), cv2.FONT
HERSHEY
COMPLEX, 1, (0, 255, 0)