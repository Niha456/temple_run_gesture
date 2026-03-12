import cv2
import time
from gesture_detection import GestureDetector
import emulator_control as emulator


def main():

    print("STARTING GESTURE CONTROL FOR EMULATOR")

    detector = GestureDetector()
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Camera not detected")
        return

    last_action = 0
    cooldown = 0.4

    while True:

        ret, frame = cap.read()
        if not ret:
            break

        gesture, frame = detector.detect_gesture(frame)

        now = time.time()

        if gesture and now - last_action > cooldown:

            if gesture == "right":
                print("RIGHT")
                emulator.move_right()

            elif gesture == "left":
                print("LEFT")
                emulator.move_left()

            elif gesture == "up":
                print("JUMP")
                emulator.jump()

            elif gesture == "down":
                print("SLIDE")
                emulator.slide()

            last_action = now

        cv2.imshow("Gesture Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()