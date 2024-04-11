import cv2
import face_recognition as fr
import numpy as np
import os
import pickle

# Tải mô hình từ file
with open('encoding_face.pkl', 'rb') as f:
    encodeListKnown = pickle.load(f)
    pics = pickle.load(f)


# startup video capture

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('video_test.mp4')


while True:

    ret, frame = cap.read()

    # frame = cv2.resize(frame, (0, 0), None, fx=0.5, fy=0.5)
    frameS = cv2.resize(frame, (0, 0), None, fx=0.5, fy=0.5)
    frameS = cv2.cvtColor(frameS, cv2.COLOR_BGR2RGB)

    faceCurFrame = fr.face_locations(frameS)
    encodeCurFrame = fr.face_encodings(frameS)

    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = fr.compare_faces(encodeListKnown, encodeFace)
        faceDis = fr.face_distance(encodeListKnown, encodeFace)
        # print(faceDis)

        matchIndex = np.argmin(faceDis)  # day ve index nho nhat
        # print(matchIndex)

        if faceDis[matchIndex] < 0.50:
            # name = classNames[matchIndex].upper()
            frameName = pics[matchIndex]
            name = frameName.split('_')[0]
        else:
            name = 'unknown'

        # rectangles
        y1, x2, y2, x1 = faceLoc
        y1, x2, y2, x1 = y1*2, x2*2, y2*2, x1*2

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, name, (x2, y2),
                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

    cv2.imshow('window', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
