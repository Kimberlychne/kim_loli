import json 
from pathlib import Path

BASE_DIR = Path(__file__).parent
file_path = BASE_DIR / "restaurant_data.json"

def load_data(file_path):
    with open(file_path, "r") as file:
        restaurant_data =json.load(file)
        return restaurant_data

def save_data(file_path, restaurant_file):
    with open(file_path, "w") as file:
        json.dump(restaurant_file,file,indent = 3)

def close_program(*args):
    print("Thanks for dining with us... Goodbye!")
    exit() 