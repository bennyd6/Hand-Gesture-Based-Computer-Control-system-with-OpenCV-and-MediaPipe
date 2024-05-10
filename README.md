Hand Gesture Based Computer Control system with OpenCV and MediaPipe
-----------------------------------------------------------------------------

This Python project allows you to control your computer's mouse cursor using hand gestures captured from your webcam. It utilizes the OpenCV library for computer vision and MediaPipe for hand landmark detection.

-----------------------------------------------------------------------------

Requirements:

Python 3.x

OpenCV library (install using pip install opencv-python)

MediaPipe library (install using pip install mediapipe)

pyautogui library (install using pip install pyautogui)


-----------------------------------------------------------------------------


How to Use?

1) Clone the repository:
git clone https://github.com/bennyd6/Hand-Gesture-Based-Computer-Control-system-with-OpenCV-and-MediaPipe.git

2) Run the script:
python hand_mouse_control.py



-----------------------------------------------------------------------------

Note: Depending on your system configuration, you might need to run the script with administrative privileges.


-----------------------------------------------------------------------------


Functionality:

The program detects the following hand gestures and performs corresponding mouse actions:

Move finger: Move the index finger to control the mouse cursor movement.

Left click: Touch the middle fingertip while having the index finger close to the middle finger and the ring finger far apart.

Recent Tabs: Touch the thumb close to the index finger (like a pincer grip).

Right Click: Touch the pinky finger close to the thumb.

Double Click: Touch the pinky finger close to the index finger vertically and horizontally far apart (like a peace sign with the pinky extended).


-----------------------------------------------------------------------------



Additional Notes

The accuracy of hand gesture detection can be affected by lighting conditions, hand pose variations, and occlusion.

The script continuously reads frames from the webcam, so expect some processing delay.

This is a basic example, and you can extend it to recognize more gestures and perform different mouse actions.
