# handcontrol
🎮 Hand Gesture Game Controller

Control ANY PC game using only your hand gestures and a webcam.
Uses OpenCV, MediaPipe 0.8.11, and PyDirectInput for real-time keyboard simulation.








✋ What This Project Does

This project lets you control games like:

Hill Climb Racing

GTA

CarX

Asphalt

Any PC game using arrow keys

by using hand gestures instead of a keyboard.

Your webcam → detects hand → gesture logic → keyboard keys.

No extra hardware. No controller. Just your hand.

🖐️ Gesture Controls
Gesture	Meaning	Sends Key
✊ Fist (0 fingers)	Brake	⬅ Left Arrow
🖐 Open Hand (5 fingers)	Gas	➡ Right Arrow

Works in fullscreen games because we use PyDirectInput.

📂 Project Structure
gesture-control/
│
├── handcontrolmain.py          # Main gesture detection + webcam
├── handcontroldirectkey.py     # Keyboard pressing (PyDirectInput)
└── README.md                   # This file


These two .py files are all you need.

🛠 Installation
❗IMPORTANT — Fix broken MediaPipe first

If you installed the wrong version, remove it:

pip uninstall mediapipe tensorflow keras -y

✔ Install correct dependencies:
pip install mediapipe==0.8.11
pip install opencv-python
pip install pydirectinput


That's it.

▶️ Run the Program
python handcontrolmain.py


A webcam window will open.
Move your hand in front of the camera.
Game will respond instantly.

Press Q to quit.

🧠 How It Works

OpenCV captures webcam frames

MediaPipe detects 21 hand landmarks

Code counts number of raised fingers

If 0 → Brake

If 5 → Gas

PyDirectInput sends real keyboard events to the game

Works on Windows fullscreen games
(Unlike the keyboard module which fails in many games).

🐞 Troubleshooting
❗ Webcam black / not opening

Your Python install needs DirectShow:

cv2.VideoCapture(0, cv2.CAP_DSHOW)

❗ MediaPipe error:

MessageFactory has no attribute GetPrototype
or
TensorFlow / Keras crash
or
MemoryError

👉 You installed wrong MediaPipe.
Install ONLY:

mediapipe==0.8.11

❗ Keys not working in-game

PyDirectInput MUST be used (your project already uses it).
