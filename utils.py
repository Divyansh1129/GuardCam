import cv2
import os
from datetime import datetime


def create_folders():
    os.makedirs("Snapshots", exist_ok=True)
    os.makedirs("Videos", exist_ok=True)


def get_timestamp():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


def get_filename():
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def save_snapshot(frame):
    filename = f"Snapshots/snapshot_{get_filename()}.jpg"
    cv2.imwrite(filename, frame)
    return filename