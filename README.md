GuardCam - Smart Security Camera

GuardCam is a Smart Security Camera built using Python and OpenCV that performs real-time motion detection and face detection through a webcam. The application automatically captures snapshots, records videos during security events, and displays live surveillance information with timestamps.

---

Features

- Real-time webcam monitoring
- Motion detection using OpenCV
- Face detection using Haar Cascade Classifier
- Automatic snapshot capture
- Automatic video recording
- Live timestamp display
- Recording indicator (REC)
- Security status display:
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

Clone the repository:

git clone https://github.com/Divyansh1129/GuardCam.git

Go to the project directory:

cd GuardCam

Install the required packages:

pip install -r requirements.txt

Run the project:

python main.py

---

How It Works

1. The webcam captures live video frames.
2. Motion detection identifies movement.
3. Face detection confirms the presence of a person.
4. When a person is detected:
   - A face bounding box is drawn.
   - The status changes to PERSON DETECTED.
   - A snapshot is saved automatically.
   - Video recording starts automatically.
5. Recording continues for a few seconds after motion stops before ending.

---

Future Improvements

- Face Recognition
- Email Alerts
- Intruder Alarm
- Cloud Storage Integration
- Multiple Camera Support
- Mobile Notifications
- Web Dashboard

---

Author

Divyansh Kaushik

- GitHub: https://github.com/Divyansh1129

---

License

This project is intended for educational and learning purposes.