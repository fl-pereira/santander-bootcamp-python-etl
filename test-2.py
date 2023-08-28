import pandas as pd
import requests
import json

data_frame = pd.read_csv('data/SBP2023.csv')
user_ids  = data_frame['UserID'].tolist()
api_url = 'https://64e7b5e1b0fd9648b7904675.mockapi.io'

print(user_ids)

def get_user(id):
    response = requests.get(f'{api_url}/etl/{id}')
    return response.json() if response.status_code == 200 else None

def change_name(id, name):
    

def update_user(id):
    response = requests.put(f"{api_url}/etl/{user['id']}", json=user)
    return True if response.status_code == 200 else False

for user in user_ids:
    print(get_user(user))

