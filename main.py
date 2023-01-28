import requests

APP_ID = 'ed2e8b7'
API_KEY = 'db72511a8066004bfbb524169d730e1'
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
print(response.text)