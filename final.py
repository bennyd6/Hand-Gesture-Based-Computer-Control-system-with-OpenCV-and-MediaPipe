import cv2
import mediapipe as mp
import os
import pyautogui
camera = cv2.VideoCapture(2)
HandDetector = mp.solutions.hands.Hands()
DrawingUtils = mp.solutions.drawing_utils
ScreenWidth,ScreenHeight=pyautogui.size()
indexx=0
middlex=0
middley=0
ringy=0
while True:
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
                x = int(landmark.x*FrameWidth)
                y = int(landmark.y*FrameHeight)
                
                if id == 8:
                    cv2.circle(img=frame, center=(x,y), radius=15, color=(255, 0,0),thickness=2)
                    indexx=ScreenWidth/FrameWidth*x
                    indexy=ScreenHeight/FrameHeight*y
                    pyautogui.moveTo(indexx,indexy)


                if id==16:
                    #cv2.circle(img=frame, center=(x,y), radius=15, color=(255, 0,0),thickness=2)
                    ringx=ScreenWidth/FrameWidth*x
                    ringy=ScreenHeight/FrameHeight*y
                    #print(abs(ringy-middley))


                if id == 12:
                    cv2.circle(img=frame, center=(x,y), radius=15, color=(255, 0,0),thickness=2)
                    middlex=ScreenWidth/FrameWidth*x
                    middley=ScreenHeight/FrameHeight*y  
                    if abs(indexy-middley)<25 and ((abs(ringy-middley)>40) and (abs(ringy-middley)<310)):
                        print("Left Click")
                        pyautogui.click()
                        pyautogui.sleep(1)
                    
                

                if id==4:
                    cv2.circle(img=frame, center=(x,y), radius=15, color=(255, 0,0),thickness=2)
                    thumbx=ScreenWidth/FrameWidth*x
                    thumby=ScreenHeight/FrameHeight*y
                    #print(abs(indexx-thumbx))
                    if abs(thumbx-indexx)<40:
                        print("Recent Tabs")
                        pyautogui.hotkey('win','tab')
                        pyautogui.sleep(2)
                

                if id==20:
                    cv2.circle(img=frame, center=(x,y), radius=15, color=(255, 0,0),thickness=2)
                    littlex=ScreenWidth/FrameWidth*x
                    littley=ScreenHeight/FrameHeight*y
                    #print(abs(thumbx-littlex))
                    if abs(thumbx-littlex)<40:
                        print("Right Click")
                        pyautogui.click(button='right')
                        pyautogui.sleep(1)
                    if abs(littley-indexy)<50 and abs(littlex-indexx)>250:
                        print("Double Click")
                        pyautogui.click(clicks=2)
                        pyautogui.sleep(1)


                if id==3:
                    thumb2x=ScreenWidth/FrameWidth*x
                    thumb2y=ScreenHeight/FrameHeight*y
                    

                if id==7:
                    index2x=ScreenWidth/FrameWidth*x
                    index2y=ScreenHeight/FrameHeight*y



                

    cv2.imshow('Bennys OneId',frame)
    cv2.waitKey(1)
