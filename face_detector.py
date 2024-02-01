import cv2

face_cascade= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

imag=cv2.imread('image.jpg')

grey= cv2.cvtColor(imag,cv2.COLOR_BGR2GREY)

faces= face_cascade.detectMultiScale(grey, 1.1,4)

for(x,y,w,h) in faces:
    cv2.rectangle(imag,(x.y),(x+w,y+h),(255,0,0),2)

cv2.imshow('img',imag)
cv2.waitKey
cv2.imwrite("face_Detected.jpg",imag)
