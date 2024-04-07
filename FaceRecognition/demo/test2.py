import cv2
import face_recognition as fr
import numpy as np
import os


path = 'pic2'
images = []
classNames = []
myList = os.listdir(path)
print(myList)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')

    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])


def img_encoding(images):
    encodeList = []

    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = fr.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


encodeListKnown = img_encoding(images)
print('encoding successfully')
# print(encodeListKnown)


# startup video capture

cap = cv2.VideoCapture(1)
# cap = cv2.VideoCapture('video_test.mp4')


while True:

    ret, frame = cap.read()

    frame = cv2.resize(frame, (0, 0), None, fx=0.5, fy=0.5)
    frameS = cv2.resize(frame, (0, 0), None, fx=0.5, fy=0.5)
    frameS = cv2.cvtColor(frameS, cv2.COLOR_BGR2RGB)

    faceCurFrame = fr.face_locations(frameS)
    encodeCurFrame = fr.face_encodings(frameS)

    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = fr.compare_faces(encodeListKnown, encodeFace)
        faceDis = fr.face_distance(encodeListKnown, encodeFace)
        print(faceDis)

        matchIndex = np.argmin(faceDis)  # day ve index nho nhat
        print(matchIndex)

        if faceDis[matchIndex] < 0.30:
            name = classNames[matchIndex].upper()
        else:
            name = 'unknown'

        # rectangles
        y1, x2, y2, x1 = faceLoc
        y1, x2, y2, x1 = y1*2, x2*2, y2*2, x1*2

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
        cv2.putText(frame, name, (x2, y2),
                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

    cv2.imshow('window', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
