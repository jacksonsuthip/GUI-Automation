import os
import random
import pyautogui
import time
from dotenv import load_dotenv

# Load environment variables (if needed)
load_dotenv()

def get_random_number(start, end):
    return random.randint(start, end)

EDGE_PATH = os.environ.get('EDGE_PATH')
URL = os.environ.get('URL')

search_terms = [
    "Instagram",
    "Facebook",
    "Python",
    "GitHub",
    "YouTube",
    "LinkedIn",
    "StackOverflow",
    "C#",
    "JavaScript",
    "LeetCode",
    "AWS",
    "Azure",
    "Google Cloud",
    "gold price today in india",
    "Sensex today",
    "Nifty today"
]

# Select 50% of the list randomly
half_size = len(search_terms) // 2
print("half_size: ", half_size)
terms = random.sample(search_terms, half_size)

# Open Edge browser
os.startfile(EDGE_PATH)
time.sleep(get_random_number(3, 3))  # wait for the browser to open

# Iterate through each search term and type it into a new tab
for term in terms:
    print("Searching for: ", term)
    pyautogui.hotkey('ctrl', 't') # Open a new tab (Ctrl + T)
    time.sleep(get_random_number(1, 3))  # wait for the new tab to open
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(get_random_number(1, 3))
    pyautogui.write(URL)
    pyautogui.press('enter')
    time.sleep(get_random_number(2, 4))
    pyautogui.typewrite(term)
    time.sleep(get_random_number(2, 5))
    pyautogui.press('enter')
    time.sleep(get_random_number(2, 3))

print("Automation complete!")
