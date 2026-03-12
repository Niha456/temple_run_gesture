import cv2
import mediapipe as mp
import time


class GestureDetector:

    def __init__(self):

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.mp_draw = mp.solutions.drawing_utils

        self.last_pos = None
        self.last_time = 0
        self.cooldown = 0.35

        self.threshold = 60   # movement required

    def detect_gesture(self, frame):

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        result = self.hands.process(rgb)

        gesture = None
        h, w, _ = frame.shape

        if result.multi_hand_landmarks:

            hand = result.multi_hand_landmarks[0]

            # use INDEX FINGER TIP (landmark 8)
            x = int(hand.landmark[8].x * w)
            y = int(hand.landmark[8].y * h)

            if self.last_pos is None:
                self.last_pos = (x, y)

            lx, ly = self.last_pos
            dx = x - lx
            dy = y - ly

            now = time.time()

            if now - self.last_time > self.cooldown:

                if abs(dx) > abs(dy):

                    if dx > self.threshold:
                        gesture = "right"

                    elif dx < -self.threshold:
                        gesture = "left"

                else:

                    if dy < -self.threshold:
                        gesture = "up"

                    elif dy > self.threshold:
                        gesture = "down"

                if gesture:
                    self.last_time = now
                    self.last_pos = (x, y)

            # draw landmarks
            self.mp_draw.draw_landmarks(
                frame,
                hand,
                self.mp_hands.HAND_CONNECTIONS
            )

            # draw pointer
            cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)

        return gesture, frame