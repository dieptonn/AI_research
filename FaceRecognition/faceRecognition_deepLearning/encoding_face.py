import cv2
import face_recognition as fr
import numpy as np
import os
import pickle


path = 'dataset_capture'
images = []
classNames = []
myList = os.listdir(path)
print(myList)

pics = []

for curPer in myList:

    pics = os.listdir(f'{path}/{curPer}')
    for pic in pics:
        curPic = cv2.imread(f'{path}/{curPer}/{pic}')
        images.append(curPic)

    # persions.append(curPer)
    classNames.append(curPer)

# print(images)

print(pics)


def img_encoding(images):
    encodeList = []

    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Kiểm tra xem có khuôn mặt trong ảnh không
        face_encodings = fr.face_encodings(img)
        if face_encodings:
            encode = face_encodings[0]
            encodeList.append(encode)

    return encodeList


encodeListKnown = img_encoding(images)
print('encoding successfully')
print(encodeListKnown)


# Lưu encodeListKnown vào file
with open('encoding_face.pkl', 'wb') as f:
    pickle.dump(encodeListKnown, f)
    pickle.dump(pics, f)
