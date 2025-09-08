import os
import json
import cv2
import numpy as np

DATASET_DIRECTORY = "Gas Station\\site_3709_0618_0702_2025"
if not os.path.isdir(DATASET_DIRECTORY):
    raise FileNotFoundError(f"Directory {DATASET_DIRECTORY} does not exist.")

ann_names = os.listdir(os.path.join(DATASET_DIRECTORY, "ann"))
video_names = os.listdir(os.path.join(DATASET_DIRECTORY, "video"))

if video_names:
    for name in video_names:
        os.remove(os.path.join(DATASET_DIRECTORY, "video", name))

for ann in ann_names:
    video_name = ann.replace(".json", "")
    ann_path = os.path.join(DATASET_DIRECTORY, "ann", ann)

    with open(ann_path, "r", encoding="utf-8") as file:
        annotation_data = json.load(file)

    width = annotation_data["size"]["width"]
    height = annotation_data["size"]["height"]
    frame_count = annotation_data["framesCount"]

    print(f"Video: {video_name}, size: {width}x{height}, frames: {frame_count}")

    video_path = os.path.join(DATASET_DIRECTORY, "video", video_name)

    fourcc = cv2.VideoWriter.fourcc(*"mp4v")
    fps = 5

    video_writer = cv2.VideoWriter(video_path, fourcc, fps, (width, height))

    black_frame = np.zeros((height, width, 3), dtype=np.uint8)

    for frame_num in range(frame_count):
        video_writer.write(black_frame)
        if frame_num % 1000 == 0:
            print(f"Ready {frame_num}/{frame_count} frames")

    video_writer.release()
    print(f"Empty video saved: {video_path}")
