import cv2
import mediapipe as mp
import pyautogui
import autopy
import time
import numpy as np
from playsound import playsound
import threading

def play_click_sound():
    threading.Thread(target=playsound, args=("click.wav",), daemon=True).start()

smoothing = 9
prev_loc_x, prev_loc_y = 0, 0

click_delay = 0.5
last_click_time = 0

screen_w, screen_h = autopy.screen.size()

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    h, w, _ = img.shape

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lm_list = []
            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((cx, cy))

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            x_index, y_index = lm_list[8]
            x_thumb, y_thumb = lm_list[4]
            x_middle, y_middle = lm_list[12]

            # Convert to screen coordinates
            target_x = np.interp(x_index, [0, w], [0, screen_w])
            target_y = np.interp(y_index, [0, h], [0, screen_h])

            curr_x = prev_loc_x + (target_x - prev_loc_x) / smoothing
            curr_y = prev_loc_y + (target_y - prev_loc_y) / smoothing

            autopy.mouse.move(curr_x, curr_y)
            prev_loc_x, prev_loc_y = curr_x, curr_y

            # Draw circle on index finger
            cv2.circle(img, (x_index, y_index), 8, (0, 255, 0), cv2.FILLED)

            distance = ((x_thumb - x_index)**2 + (y_thumb - y_index)**2) ** 0.5
            current_time = time.time()

            if distance < 40 and (current_time - last_click_time) > click_delay:
                autopy.mouse.click()
                play_click_sound()
                last_click_time = current_time

            # Scroll using index-middle finger vertical distance
            scroll_distance = y_index - y_middle
            if abs(scroll_distance) > 30:
                if scroll_distance > 0:
                    pyautogui.scroll(-50)  # scroll down
                else:
                    pyautogui.scroll(50)   # scroll up

    cv2.imshow("Virtual AI Mouse", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
