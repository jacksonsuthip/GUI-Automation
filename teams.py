import os
import time
import pyautogui

time.sleep(5)

current_directory = os.path.dirname(os.path.abspath(__file__))

image_path = os.path.join(current_directory, 'assets', 'teamsCall.png')

location = pyautogui.locateOnScreen('./assets/teamsCall.png', confidence=0.5)

print(location)

if location is not None:
    center = pyautogui.center(location)
    pyautogui.click(center)
    print(f"Clicked at {center}")
else:
    print("Image not found")