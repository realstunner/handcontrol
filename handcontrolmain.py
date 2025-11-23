import cv2
import mediapipe as mp
import time
from handcontroldirectkey import RIGHT_KEY, LEFT_KEY, PressKey, ReleaseKey  

# Assign controls
brake_key_pressed = LEFT_KEY        # ← brake
accelerator_key_pressed = RIGHT_KEY # → gas

time.sleep(2.0)
current_key_pressed = set()

mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands

tipIds = [4, 8, 12, 16, 20]

video = cv2.VideoCapture(0)

with mp_hand.Hands(min_detection_confidence=0.5,
                   min_tracking_confidence=0.5) as hands:
    while True:
        keyPressed = False
        key_pressed = None
        ret, image = video.read()
        if not ret:
            break

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        lmList = []

        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                myHands = results.multi_hand_landmarks[0]
                for id, lm in enumerate(myHands.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])
                mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)

        if lmList:
            fingers = []
            # Thumb
            fingers.append(1 if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1] else 0)
            # Other fingers
            for id in range(1, 5):
                fingers.append(1 if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2] else 0)

            total = fingers.count(1)

            if total == 0:   # Fist → Brake
                cv2.putText(image, "BRAKE", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (0, 0, 255), 5)
                PressKey(brake_key_pressed)
                current_key_pressed.add(brake_key_pressed)
                key_pressed = brake_key_pressed
                keyPressed = True

            elif total == 5: # Open Palm → Gas
                cv2.putText(image, "GAS", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (0, 255, 0), 5)
                PressKey(accelerator_key_pressed)
                current_key_pressed.add(accelerator_key_pressed)
                key_pressed = accelerator_key_pressed
                keyPressed = True

        # Release logic
        if not keyPressed and current_key_pressed:
            for key in current_key_pressed:
                ReleaseKey(key)
            current_key_pressed = set()
        elif keyPressed and len(current_key_pressed) > 1:
            for key in list(current_key_pressed):
                if key != key_pressed:
                    ReleaseKey(key)
                    current_key_pressed.remove(key)

        cv2.imshow("Frame", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

video.release()
cv2.destroyAllWindows()
