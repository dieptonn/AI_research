import cv2
import time
import os
import hand as htm  # import module hand
import math
import numpy as np

from comtypes import CLSCTX_ALL  # type: ignore
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume  # type: ignore


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

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volume.GetVolumeRange()


volRange = volume.GetVolumeRange()
print(volRange)

minVol = volRange[0]
maxVol = volRange[1]

while True:
    ret, frame = cap.read()
    frame = detector.findHands(frame)
    lmList = detector.findPosition(frame, draw=False)  # phát hiện vị trí

    if len(lmList) != 0:

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]

        cv2.circle(frame, (x1, y1), 15, (255, 255, 0), -1)
        cv2.circle(frame, (x2, y2), 15, (255, 255, 0), -1)

        cv2.line(frame, (x1, y1), (x2, y2), (255, 255, 0), 3)

        cx, cy = (x1+x2)//2, (y1+y2)//2
        cv2.circle(frame, (cx, cy), 15, (255, 255, 0), -1)

        length = math.hypot(x2-x1, y2-y1)
        # print(length)

        # Dai am thanh tren may
        vol = np.interp(length, [25, 230], [minVol, maxVol])
        volBar = np.interp(length, [25, 230], [180, 30])
        vol_scale = np.interp(length, [25, 230], [0, 100])

        volume.SetMasterVolumeLevel(vol, None)
        print(length, vol)

        if length < 25:
            cv2.circle(frame, (cx, cy), 15, (0, 0, 255), -1)
        if length > 230:
            cv2.circle(frame, (cx, cy), 15, (0, 0, 255), -1)

        cv2.rectangle(frame, (30, 30), (60, 180), (0, 255, 0), 1)
        cv2.rectangle(frame, (30, 180), (60, int(volBar)), (0, 255, 0), -1)

        cv2.putText(frame, f'{int(vol_scale)} %', (25, 200),
                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)

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
