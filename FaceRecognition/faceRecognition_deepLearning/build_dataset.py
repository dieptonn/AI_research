# USAGE
# python build_dataset.py --output dataset_capture/diepton

import argparse
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True,
                help="dataset_capture/")
args = vars(ap.parse_args())

# Kiểm tra xem thư mục output đã tồn tại chưa
if not os.path.exists(args["output"]):
    os.makedirs(args["output"])

video = cv2.VideoCapture(0)
total = 0
while True:
    ret, frame = video.read()

    cv2.imshow("video", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("k"):
        # Tạo đường dẫn cho ảnh với tên thư mục là args["output"]
        # và tên ảnh có dạng "args["output"]_{}.png"
        p = os.path.sep.join(
            [args["output"], "{}_{}.png".format(os.path.basename(args["output"]), str(total).zfill(5))])

        cv2.imwrite(p, frame)
        total += 1
        # nhấn q để thoát
    elif key == ord("q"):
        break

print("[INFO] {} face images stored".format(total))
video.release()
cv2.destroyAllWindows()
