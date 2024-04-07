import cv2
import os
import face_recognition as fr
import numpy as np

imgElon = fr.load_image_file('pic/elon_musk.jpg')
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)

imgCheck = fr.load_image_file('pic/elon_check.jpg')
imgCheck = cv2.cvtColor(imgCheck, cv2.COLOR_BGR2RGB)

# xác định vị trí khuôn mặt

faceLocation = fr.face_locations(imgElon)[0]
print(faceLocation)  # (y1,x2,y2,x1)


# ma hoa hinh anh
encodeElon = fr.face_encodings(imgElon)[0]
cv2.rectangle(
    imgElon, (faceLocation[3], faceLocation[0]), (faceLocation[1], faceLocation[2]), (0, 255, 0), 1)


# xác định vị trí khuôn mặt

faceCheck = fr.face_locations(imgCheck)[0]
print(faceCheck)  # (y1,x2,y2,x1)


# ma hoa hinh anh
encodeCheck = fr.face_encodings(imgCheck)[0]
cv2.rectangle(
    imgCheck, (faceCheck[3], faceCheck[0]), (faceCheck[1], faceCheck[2]), (0, 255, 0), 1)


results = fr.compare_faces([encodeElon], encodeCheck)

faceDis = fr.face_distance([encodeElon], encodeCheck)
cv2.putText(imgCheck, f'{results}~{1- round(faceDis[0],2)}', (
    30, 30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 1)


print(results, faceDis)


cv2.imshow('Elon Mask', imgElon)
cv2.imshow('Elon Check', imgCheck)

cv2.waitKey()
