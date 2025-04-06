import os
import pyautogui
import time
from dotenv import load_dotenv

# load_dotenv()
load_dotenv(".env.example")

MESSAGES = os.environ.get('MESSAGES')

messagesList = MESSAGES.split(',') if MESSAGES else []

time.sleep(5)

for message in messagesList:
    split_msg = message.split(":")

    pyautogui.typewrite(":" + split_msg[1])
    time.sleep(7)
    pyautogui.press("enter")
    pyautogui.typewrite(split_msg[2])
    time.sleep(2)
    pyautogui.press("enter")
    print(f"Message {message} sent")

print("Automation complete!")
