import os
import requests
from datetime import datetime

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

GENDER = "male"
WEIGHT = 80
HEIGHT = 190
AGE = 30

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = f"{os.environ['SHEET_ENDPOINT']}"

exercise_text = input("What exercises was that?\n")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=params, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result['exercises']:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise['name'].title(),
            "duration": f"{str(exercise['duration_min'])} min",
            "calories": exercise['nf_calories'],
        }
    }

# No AUTH
sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

# Basic
basic_header = {
    "Authorization": f"Basic {os.environ['TOKEN']}",
}

sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=basic_header)

# Bearer
bearer_header = {
    "Authorization": f"Bearer {os.environ['TOKEN']}",
}

sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_header)
