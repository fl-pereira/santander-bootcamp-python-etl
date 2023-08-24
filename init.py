import pandas as pd
import requests
import json

bootcamp_api_url = 'https://sdw-2023-prd.up.railway.app'

data_frame = pd.read_csv('data/SBP2023.csv')
user_ids  = data_frame['UserID'].tolist()
print(user_ids)

def get_user(id):
    response = requests.get(f'{bootcamp_api_url}/users/{id}')
    return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(users, indent=2))