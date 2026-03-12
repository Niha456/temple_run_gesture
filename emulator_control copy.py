import os

# Screen center (based on your resolution ~1842x1048)
CENTER_X = 900
CENTER_Y = 500

def move_left():
    os.system("adb shell input swipe 900 500 400 500 100")

def move_right():
    os.system("adb shell input swipe 900 500 1400 500 100")

def jump():
    os.system("adb shell input swipe 900 700 900 300 100")

def slide():
    os.system("adb shell input swipe 900 300 900 700 100")