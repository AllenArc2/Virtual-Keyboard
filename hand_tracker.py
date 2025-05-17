import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self, maxHands=1):
        self.hands = mp.solutions.hands.Hands(max_num_hands=maxHands)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        hands_landmarks = []
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                lmList = []
                for id, lm in enumerate(handLms.landmark):
                    h, w, _ = img.shape
                    lmList.append((int(lm.x * w), int(lm.y * h)))
                hands_landmarks.append(lmList)
                self.mpDraw.draw_landmarks(img, handLms, mp.solutions.hands.HAND_CONNECTIONS)
        return img, hands_landmarks
