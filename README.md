GuardCam - Smart Security Camera

GuardCam is a Smart Security Camera built using Python and OpenCV that performs real-time motion detection and face detection through a webcam. The application automatically captures snapshots, records videos during detection events, and displays live surveillance status with timestamps.

---

Features

- Real-time webcam surveillance
- Motion detection
- Face detection using Haar Cascade Classifier
- Automatic snapshot capture
- Automatic video recording
- Live timestamp display
- Recording status indicator
- Security status monitoring
  - SAFE
  - MOTION DETECTED
  - PERSON DETECTED
- Automatic recording stop after inactivity
- Automatic creation of Snapshots and Videos folders

---

Technologies Used

- Python
- OpenCV
- NumPy

---

Project Structure

GuardCam/
│
├── main.py
├── motion_detector.py
├── face_detector.py
├── recorder.py
├── utils.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── Snapshots/
└── Videos/

---

Installation

Clone the repository

git clone https://github.com/Divyansh1129/GuardCam.git

Navigate to the project directory

cd GuardCam

Install the required dependencies

pip install -r requirements.txt

Run the project

python main.py

---

How It Works

1. Captures live video from the webcam.
2. Detects motion in the video stream.
3. Detects faces when motion occurs.
4. Displays the current surveillance status.
5. Automatically saves a snapshot when a person is detected.
6. Starts recording the video automatically.
7. Stops recording a few seconds after no motion is detected.

---

Screenshots

Create an "assets" folder inside the project directory and add screenshots.

Example:

assets/
├── home.png
├── person_detected.png
└── recording.png

Then add them to the README like this:

## Home Screen

![Home](assets/home.png)

## Person Detected

![Person Detected](assets/person_detected.png)

## Recording

![Recording](assets/recording.png)

---

Future Improvements

- Face Recognition
- Email Notifications
- SMS Alerts
- Cloud Storage Integration
- Multiple Camera Support
- Web Dashboard
- Mobile Application

---

Author

Divyansh Kaushik

GitHub: https://github.com/Divyansh1129

---

License

This project is intended for educational and learning purposes.
