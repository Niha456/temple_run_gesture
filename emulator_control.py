import os

# ----------------------------
# EMULATOR CONTROL FUNCTIONS
# ----------------------------

# # Option 1: Using ydotool (requires sudo to start ydotoold)
# def move_left():
#     os.system("sudo ydotool key 105:1 105:0")
#     # os.system("adb shell input swipe 900 500 400 500 120")

# def move_right():
#     os.system("sudo ydotool key 106:1 106:0")
#     # os.system("adb shell input swipe 400 500 900 500 120")

# def jump():
#     os.system("sudo ydotool key 103:1 103:0")
#     # os.system("adb shell input swipe 900 750 900 350 120")

# def slide():
#     os.system("sudo ydotool key 108:1 108:0")
#     # os.system("adb shell input swipe 900 350 900 750 120")

# Option 2: Using ADB swipe (recommended for Waydroid/Genymotion)
# Uncomment these lines to use ADB swipes instead of ydotool

def move_left():
    os.system("adb shell input swipe 900 500 400 500 120")

def move_right():
    os.system("adb shell input swipe 400 500 900 500 120")

def jump():
    os.system("adb shell input swipe 900 750 900 350 120")

def slide():
    os.system("adb shell input swipe 900 350 900 750 120")
