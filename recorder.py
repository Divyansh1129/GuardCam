import cv2
from datetime import datetime


class VideoRecorder:

    def __init__(self):
        self.recording = False
        self.writer = None

    def start(self, frame_width, frame_height):

        if self.recording:
            return

        filename = datetime.now().strftime(
            "Videos/video_%Y%m%d_%H%M%S.mp4"
        )

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')

        self.writer = cv2.VideoWriter(
            filename,
            fourcc,
            20.0,
            (frame_width, frame_height)
        )

        self.recording = True

        print(f"Recording Started : {filename}")

    def write(self, frame):

        if self.recording:
            self.writer.write(frame)

    def stop(self):

        if self.recording:
            self.writer.release()
            self.writer = None
            self.recording = False
            print("Recording Stopped")