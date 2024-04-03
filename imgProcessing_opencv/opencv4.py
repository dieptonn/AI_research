import cv2
import numpy as np

cap = cv2.VideoCapture('sample.mp4')
while True:
    ret, frame = cap.read()
    # print(ret)
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (0, 0), (width, height), (0, 0, 255), 1)
    img = cv2.line(frame, (0, height), (width, 0), (255, 0, 0), 1)
    img = cv2.line(frame, (0, height//2), (width, height//2), (0, 255, 0), 1)
    img = cv2.line(frame, (width//2, 0), (width//2, height), (200, 125, 70), 1)
    img = cv2.rectangle(frame, (width//4, height//4),
                        (3*width//4, 3*height//4), (255, 255, 255), 5)

    img = cv2.circle(frame, (width//2, height//2),
                     height//2, (200, 165, 15), 3)

    # Nếu độ dày của đường kẻ = -1 thì sẽ tô màu toàn khối
    font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    img = cv2.putText(frame, 'okay', (10, 100), font, 1, (255, 255, 255))

    cv2.imshow('cua so cam', frame)
    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
