import cv2


class MotionDetector:

    def __init__(self):

        self.background = cv2.createBackgroundSubtractorMOG2(
            history=500,
            varThreshold=40,
            detectShadows=False
        )

    def detect_motion(self, frame):

        mask = self.background.apply(frame)

        kernel = cv2.getStructuringElement(
            cv2.MORPH_RECT,
            (5, 5)
        )

        mask = cv2.morphologyEx(
            mask,
            cv2.MORPH_OPEN,
            kernel
        )

        mask = cv2.dilate(
            mask,
            kernel,
            iterations=2
        )

        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        motion = False
        boxes = []

        for contour in contours:

            area = cv2.contourArea(contour)

            if area < 5000:
                continue

            x, y, w, h = cv2.boundingRect(contour)

            if w < 70 or h < 70:
                continue

            aspect_ratio = w / h

            if aspect_ratio > 2.5 or aspect_ratio < 0.3:
                continue

            motion = True

            boxes.append((x, y, w, h))

        return motion, boxes