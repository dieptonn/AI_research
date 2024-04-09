import os
import cv2
import shutil
import random


def capture_frames(video_path, output_train_dir, output_test_dir, num_frames, train_ratio=0.8):

    cap = cv2.VideoCapture(video_path)

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_indices = random.sample(
        range(frame_count), min(num_frames, frame_count))

    for idx in frame_indices:

        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = cap.read()

        if ret:
            # Quyết định xem frame này thuộc phần train hay test dựa trên train_ratio
            if random.random() < train_ratio:
                output_dir = output_train_dir
            else:
                output_dir = output_test_dir

            frame_path = os.path.join(output_dir, f"frame_{idx}.jpg")

            # Kiểm tra xem frame đã tồn tại trong thư mục hay chưa
            if not os.path.exists(frame_path):
                cv2.imwrite(frame_path, frame)

    cap.release()


def split_data(dataset_dir, train_dir, test_dir, train_ratio=0.8):

    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    for person_dir in os.listdir(dataset_dir):

        person_data_dir = os.path.join(dataset_dir, person_dir)

        if os.path.isdir(person_data_dir):

            person_train_dir = os.path.join(
                train_dir, os.path.basename(person_dir))
            person_test_dir = os.path.join(
                test_dir, os.path.basename(person_dir))

            # Kiểm tra xem thư mục train và test đã tồn tại hay chưa
            if not os.path.exists(person_train_dir) and not os.path.exists(person_test_dir):

                os.makedirs(person_train_dir)
                os.makedirs(person_test_dir)
            else:   # Nếu cả hai thư mục đã tồn tại
                continue

            for video_file in os.listdir(person_data_dir):

                video_path = os.path.join(person_data_dir, video_file)

                output_train_dir = person_train_dir
                output_test_dir = person_test_dir

                capture_frames(video_path, output_train_dir,
                               output_test_dir, num_frames_per_video)


if __name__ == "__main__":
    dataset_dir = "dataset"
    train_dir = "train"
    test_dir = "test"
    num_frames_per_video = 30

    split_data(dataset_dir, train_dir, test_dir)
