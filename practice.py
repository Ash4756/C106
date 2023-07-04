# import the opencv library
import cv2
img = cv2.imread("boy.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Load the Cascade Classifier File
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
# Detect the faces
faces = face_cascade.detectMultiScale(gray, 1.1, 5)
print(len(faces))
# Draw the rectangle around each face
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    roi_color = img[y:y+h,x:x+w]  
    cv2.imwrite("face.jpg",roi_color)  
# Display the resulting frame
cv2.imshow('img', img)
cv2.waitKey(0)
