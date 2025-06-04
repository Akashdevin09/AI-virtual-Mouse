# 🖱️ AI Virtual Mouse using Hand Gestures

This project implements an **AI-based virtual mouse system** that uses **real-time hand gesture recognition** to control mouse functions such as cursor movement, clicking, and scrolling—**without the need for physical contact**. It leverages **computer vision and machine learning** to enable hands-free control through a standard webcam.

---

## Features

* 🖐️ **Hand Tracking**: Utilizes **MediaPipe** to detect and track hand landmarks in real-time.
* 🎯 **Cursor Movement**: Move the mouse cursor smoothly using the index finger.
* 🖱️ **Click Detection**: Perform mouse clicks by pinching the **thumb and index finger** together.
* 🧭 **Scroll Control**: Scroll up or down by moving the **index and middle fingers** apart or together.
* 🔊 **Audio Feedback**: Integrated **click sound feedback** using `pygame` for better user experience.
* 🎥 **Live Camera Feed**: Visualizes hand landmarks and gestures via OpenCV GUI.

---

## 🛠️ Tech Stack

| Component       | Library Used                                     |
| --------------- | ------------------------------------------------ |
| Hand Tracking   | [MediaPipe](https://github.com/google/mediapipe) |
| Computer Vision | OpenCV                                           |
| Mouse Control   | AutoPy & PyAutoGUI                               |
| Audio Feedback  | Pygame                                           |
| Multi-threading | Python `threading` module                        |

---

## 📂 Project Structure

```
AI-Virtual-Mouse/
│
├── main.py                 # Main script for gesture recognition and control
├── click.wav              # Custom sound for click feedback
├── requirements.txt       # List of required Python packages
└── README.md              # Project documentation (you are here!)
```

---

## 🔧 Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/AI-Virtual-Mouse.git
cd AI-Virtual-Mouse
```

2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Make sure `click.wav` is in the root directory. If missing, add your own `.wav` file named `click.wav`.

---

## ▶️ How to Run

```bash
python main.py
```

Ensure your webcam is connected. The app will open a window displaying the camera feed with hand tracking.

* Use your **index finger** to move the cursor.
* Pinch your **thumb and index finger** to simulate a click.
* Move **index and middle fingers** vertically apart to scroll.

Press `Q` to exit.

---


## 📖 Future Improvements

* Add multi-hand support
* Implement gesture-based drag and drop
* Support custom gestures for keyboard shortcuts
* Add GUI for calibration and control

---

## 👨‍💻 Author

**Akash**
[GitHub](https://github.com/Akashdevin09) | [LinkedIn](https://www.linkedin.com/in/akash-mishra-5b9452287/)

---

Let me know if you'd like a `README.md` version or help with creating the GitHub repo and uploading.
