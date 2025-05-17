import cv2
import pyautogui

class VirtualKeyboard:
    def __init__(self):
        self.keys = [
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O'],
            ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
            ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
        ]
        self.key_size = (60, 60)
        self.key_coords = []

    def draw(self, img):
        self.key_coords = []
        for i, row in enumerate(self.keys):
            for j, key in enumerate(row):
                x = j * (self.key_size[0] + 5) + 50
                y = i * (self.key_size[1] + 5) + 50
                self.key_coords.append((key, (x, y)))
                cv2.rectangle(img, (x, y), (x + self.key_size[0], y + self.key_size[1]), (255, 0, 0), -1)
                cv2.putText(img, key, (x + 20, y + 40), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

    def check_key_press(self, index_finger_tip, click):
        for key, (x, y) in self.key_coords:
            x1, y1 = x, y
            x2, y2 = x + self.key_size[0], y + self.key_size[1]

            if x1 < index_finger_tip[0] < x2 and y1 < index_finger_tip[1] < y2:
                if click:
                    print(f"Simulating key press: {key}")
                    pyautogui.press(key.lower())
                    return key
        return None
