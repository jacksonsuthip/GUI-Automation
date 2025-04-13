import os
import random
import pyautogui
import time
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables (if needed)
load_dotenv()

def get_random_number(start, end):
    return random.randint(start, end)

start_time = datetime.now()
print(f"Start Time: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

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
    "Sensex today in india",
    "Nifty today in india",
    "Bitcoin price today in india",
    "Dollar price today in india",
    "TypeScript",
    "Node.js",
    "React",
    "Django",
    "Flask",
    "Spring Boot",
    "Machine Learning",
    "ChatGPT",
    "OpenAI",
    "Google Bard",
    "Stable Diffusion",
    "Firebase",
    "DigitalOcean",
    "Snowflake",
    "PostgreSQL",
    "Apache Kafka",
    "BigQuery",
    "Crypto market today in india",
    "Top gainers in stock market today",
    "INR to USD today",
    "Weather today in Delhi",
    "Weather today in Bangalore",
    "Codeforces",
    "GeeksforGeeks",
    "Toy Story",
    "The Lion King",
    "Frozen",
    "Moana",
    "Inside Out",
    "Encanto",
    "Coco",
    "Ratatouille",
    "WALL-E",
    "Kung Fu Panda",
    "The Incredibles",
    "Despicable Me",
    "Tangled",
    "Spider-Man: Into the Spider-Verse",
    "Spirited Away"
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
    time.sleep(get_random_number(3, 5))

end_time = datetime.now()
duration = (end_time - start_time).total_seconds()

print(f"End Time:   {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Duration:   {duration:.2f} seconds")
print("Automation complete!")
