import cv2
import time
from motion_detector import MotionDetector
from face_detector import FaceDetector
from recorder import VideoRecorder
from utils import create_folders, get_timestamp, save_snapshot

create_folders()

motion_detector = MotionDetector()
face_detector = FaceDetector()
recorder = VideoRecorder()

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Unable to access webcam.")
    exit()

cv2.namedWindow("GuardCam", cv2.WINDOW_NORMAL)
cv2.resizeWindow("GuardCam", 900, 600)

ret, frame = camera.read()

if not ret:
    print("Unable to read camera.")
    camera.release()
    exit()

frame_height, frame_width = frame.shape[:2]

snapshot_taken = False
last_motion_time = 0

while True:

    ret, frame = camera.read()

    if not ret:
        break

    motion_detected, motion_boxes = motion_detector.detect_motion(frame)

    faces = face_detector.detect_faces(frame)

    person_detected = motion_detected and len(faces) > 0

    for x, y, w, h in motion_boxes:

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)

    for x, y, w, h in faces:

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        cv2.putText(
            frame, "FACE", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2
        )

    cv2.putText(
        frame, "GUARDCAM", (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2
    )

    if person_detected:

        status = "STATUS : PERSON DETECTED"
        color = (0, 0, 255)

        last_motion_time = time.time()

        cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), (0, 0, 255), 4)

        recorder.start(frame_width, frame_height)
        recorder.write(frame)

    elif motion_detected:

        status = "STATUS : MOTION DETECTED"
        color = (0, 165, 255)

        snapshot_taken = False

        if recorder.recording:

            recorder.write(frame)

            if time.time() - last_motion_time >= 5:
                recorder.stop()

    else:

        status = "STATUS : SAFE"
        color = (0, 255, 0)

        snapshot_taken = False

        if recorder.recording:

            recorder.write(frame)

            if time.time() - last_motion_time >= 5:
                recorder.stop()

    cv2.putText(frame, status, (20, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.putText(
        frame,
        get_timestamp(),
        (20, 110),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2,
    )

    if recorder.recording:

        cv2.circle(frame, (30, 145), 8, (0, 0, 255), -1)

        cv2.putText(
            frame, "REC", (45, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2
        )

    if person_detected and not snapshot_taken:

        filename = save_snapshot(frame)

        print(f"Snapshot Saved : {filename}")

        snapshot_taken = True

    cv2.imshow("GuardCam", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

recorder.stop()
camera.release()
cv2.destroyAllWindows()
