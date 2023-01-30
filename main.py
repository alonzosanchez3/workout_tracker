import requests
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv('APP_ID')
print(APP_ID)
API_KEY = os.getenv('API_KEY')
print(API_KEY)
exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
GENDER = "male"
WEIGHT_KG = 99.1
HEIGHT_CM = 176.1
AGE = 28


headers = {
  'x-app-id': APP_ID,
  'x-app-key': API_KEY,
  'Content-Type': 'application/json'
}

query = input('Tell me which exercises you did: ')

exercise_config = {
  'query': query,
  'gender': GENDER,
  'weight_kg': WEIGHT_KG,
  'height_cm': HEIGHT_CM,
  'age': AGE
}

response = requests.post(url=exercise_endpoint, json=exercise_config, headers=headers)
data = response.json()['exercises']

now = dt.datetime.now()
todays_date = now.strftime("%d/%m/%Y")
workout_time = now.strftime('%H:%M:%S')
workout = data[0]["name"].title()
duration = data[0]['duration_min']
calories = data[0]['nf_calories']


sheety_endpoint = os.getenv('SHEETY_ENDPOINT')

sheety_config = {
  'workout': {
    'date': todays_date,
    'time': workout_time,
    'exercise': workout,
    'duration': duration,
    'calories': calories
  }
}

sheety_headers = {
  "Authorization": f"Bearer {os.getenv('BEARER')}"
}

response = requests.post(url=sheety_endpoint, json=sheety_config, headers=sheety_headers)
response.raise_for_status()
