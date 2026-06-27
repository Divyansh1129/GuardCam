# GuardCam - Smart Security Camera

GuardCam is a smart security camera application built with **Python** and **OpenCV** that provides real-time surveillance using your webcam. It detects motion and faces, automatically captures snapshots, records video during security events, and displays live monitoring information with timestamps.

---

## Features

* Real-time webcam surveillance
* Motion detection using frame differencing
* Face detection using OpenCV Haar Cascade Classifier
* Automatic snapshot capture when a person is detected
* Automatic video recording during detection events
* Live timestamp overlay
* Recording status indicator
* Security status monitoring

  * **SAFE**
  * **MOTION DETECTED**
  * **PERSON DETECTED**
* Automatic recording stop after inactivity
* Automatically creates `Snapshots` and `Videos` folders

---

## Technologies Used

* Python
* OpenCV
* NumPy

---

## Project Structure

```text
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
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Divyansh1129/GuardCam.git
```

### 2. Navigate to the Project Directory

```bash
cd GuardCam
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python main.py
```

---

## How It Works

1. Opens the webcam and starts live surveillance.
2. Continuously monitors frames for motion.
3. Detects faces whenever motion is present.
4. Updates the surveillance status in real time.
5. Captures a snapshot when a face is detected.
6. Starts recording the video automatically.
7. Stops recording after a short period of inactivity.

---

## Screenshots

Create an `assets` folder inside the project directory and add your screenshots.

```text
assets/
├── home.png
├── person_detected.png
└── recording.png
```

Then include them in the README as shown below.

### Home Screen

<p align="center">
  <img src="assets/home.png" alt="Home Screen" width="850">
</p>

---

### Person Detected

<p align="center">
  <img src="assets/person_detected.png" alt="Person Detected" width="850">
</p>

---

### Recording

<p align="center">
  <img src="assets/recording.png" alt="Recording" width="850">
</p>

---

## Future Improvements

* Face Recognition
* Email Notifications
* SMS Alerts
* Cloud Storage Integration
* Multiple Camera Support
* Web Dashboard
* Mobile Application

---

## Requirements

Install the required Python packages:

```text
opencv-python
numpy
```

Or simply run:

```bash
pip install -r requirements.txt
```

---

## Author

**Divyansh Kaushik**

GitHub: https://github.com/Divyansh1129

---

## License

This project is intended for educational and learning purposes.

You are free to use, modify, and extend the project for personal or academic use.
