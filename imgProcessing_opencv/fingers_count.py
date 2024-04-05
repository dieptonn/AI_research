import cv2
import time
import os
import hand as htm  # import module hand


pTime = 0
cap = cv2.VideoCapture(0)

FolderPath = 'Fingers'
lst = os.listdir(FolderPath)
lst_2 = []


for i in lst:
    image = cv2.imread(f'{FolderPath}/{i}')
    # print(image)
    lst_2.append(image)

print(lst_2[0].shape)

detector = htm.handDetector(detectionCon=1)

fingerid = [4, 8, 12, 16, 20]

while True:
    ret, frame = cap.read()

    frame = detector.findHands(frame)
    lmList = detector.findPosition(frame, draw=False)  # phát hiện vị trí
    # print(lmList)
    if detector.results and detector.results.multi_hand_landmarks:
        if len(detector.results.multi_hand_landmarks) > 1:
            print('Nhận diện được cả hai tay')
        elif len(detector.results.multi_hand_landmarks) == 1:
            print('Nhận diện được một tay')
    else:
        print('Không nhận diện được bàn tay')

    print(len(lmList))

    if len(lmList) != 0:
        fingers = []

        if lmList[fingerid[0]][1] < lmList[fingerid[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1, 5):
            if lmList[fingerid[id]][2] < lmList[fingerid[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        # print(fingers)
        so_ngon_tay = fingers.count(1)
        # print(so_ngon_tay)

        h, w, c = lst_2[so_ngon_tay-1].shape
        frame[0:h, 0:w] = lst_2[so_ngon_tay-1]

        cv2.rectangle(frame, (0, h), (w//2, 3*h//2), (0, 255, 0), -1)
        cv2.putText(frame, str(so_ngon_tay), (w//5, 5*h//4),
                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)

    # show fps
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(frame, f'FPS: {int(fps)}', (550, 30),
                cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)

    cv2.imshow('cua so cam', frame)
    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
