import cv2
import time
import numpy as np
from hand_tracker import HandDetector
from virtual_keyboard import VirtualKeyboard
import math

cap = cv2.VideoCapture(0)
detector = HandDetector()
keyboard = VirtualKeyboard()

last_click_time = 0
cooldown = 0.5  # seconds

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame, hands = detector.findHands(frame)

    if hands:
        lmList = hands[0]  # Only use first hand
        index_tip = lmList[8]  # Index finger tip
        thumb_tip = lmList[4]  # Thumb tip

        # Draw circles to debug
        cv2.circle(frame, index_tip, 10, (0, 0, 255), -1)
        cv2.circle(frame, thumb_tip, 10, (255, 0, 0), -1)

        # Measure distance
        dist = math.hypot(index_tip[0] - thumb_tip[0], index_tip[1] - thumb_tip[1])
        print("Distance:", dist)
        click = dist < 60

        # Click detection with cooldown
        current_time = time.time()
        if click and (current_time - last_click_time > cooldown):
            key_pressed = keyboard.check_key_press(index_tip, click)
            if key_pressed:
                print(f"Key Pressed: {key_pressed}")
            last_click_time = current_time

    # Draw keyboard
    keyboard.draw(frame)

    cv2.imshow("Virtual Keyboard", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
