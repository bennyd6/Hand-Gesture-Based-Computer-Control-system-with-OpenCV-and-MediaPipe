from flask import Flask, render_template, Response, jsonify
import cv2
import mediapipe as mp
import wx
# import pyautogui

app = Flask(__name__)

camera = cv2.VideoCapture(1)
HandDetector = mp.solutions.hands.Hands()
DrawingUtils = mp.solutions.drawing_utils
ScreenWidth, ScreenHeight = wx.GetDisplaySize()

def process_frame():
    indexx = 0
    indexy = 0
    middlex = 0
    middley = 0
    ringy = 0

    ref, frame = camera.read()
    frame = cv2.flip(frame, 1)
    FrameHeight, FrameWidth, _ = frame.shape
    rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = HandDetector.process(rgbFrame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            DrawingUtils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * FrameWidth)
                y = int(landmark.y * FrameHeight)

                if id == 8:
                    cv2.circle(img=frame, center=(x, y), radius=15, color=(255, 0, 0), thickness=2)
                    indexx = ScreenWidth / FrameWidth * x
                    indexy = ScreenHeight / FrameHeight * y
                    # pyautogui.moveTo(indexx, indexy)

                if id == 16:
                    ringx = ScreenWidth / FrameWidth * x
                    ringy = ScreenHeight / FrameHeight * y

                if id == 12:
                    cv2.circle(img=frame, center=(x, y), radius=15, color=(255, 0, 0), thickness=2)
                    middlex = ScreenWidth / FrameWidth * x
                    middley = ScreenHeight / FrameHeight * y
                    if abs(indexy - middley) < 25 and ((abs(ringy - middley) > 40) and (abs(ringy - middley) < 310)):
                        print("Left Click")
                        # pyautogui.click()
                        # pyautogui.sleep(1)

                if id == 4:
                    cv2.circle(img=frame, center=(x, y), radius=15, color=(255, 0, 0), thickness=2)
                    thumbx = ScreenWidth / FrameWidth * x
                    thumby = ScreenHeight / FrameHeight * y
                    if abs(thumbx - indexx) < 40:
                        print("Recent Tabs")
                        # pyautogui.hotkey('win', 'tab')
                        # pyautogui.sleep(2)

                if id == 20:
                    cv2.circle(img=frame, center=(x, y), radius=15, color=(255, 0, 0), thickness=2)
                    littlex = ScreenWidth / FrameWidth * x
                    littley = ScreenHeight / FrameHeight * y
                    if abs(thumbx - littlex) < 40:
                        print("Right Click")
                        # pyautogui.click(button='right')
                        # pyautogui.sleep(1)
                    if abs(littley - indexy) < 50 and abs(littlex - indexx) > 250:
                        print("Double Click")
                        # pyautogui.click(clicks=2)
                        # pyautogui.sleep(1)

    ret, buffer = cv2.imencode('.jpg', frame)
    frame = buffer.tobytes()
    return frame

def gen_frames():
    while True:
        frame = process_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/run_cv_code', methods=['POST'])
def run_cv_code():
    frame = process_frame()
    return jsonify({"status": "CV code executed"})

if __name__ == '__main__':
    app.run(debug=True)
