import pandas as pd
import requests
import json
import openai

data_frame = pd.read_csv('data/SBP2023.csv')
user_ids  = data_frame['UserID'].tolist()

bootcamp_api_url = 'https://sdw-2023-prd.up.railway.app'

def get_user(id):
    response = requests.get(f'{bootcamp_api_url}/users/{id}')
    return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if (user := get_user(id)) is not None]

openai.api_key = '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'

def generate_ai_news(user):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Você é MUITO bom no que faz. Estou impressionado!"
            },
            {
                "role": "user",
                "content": f"Crie uma mensagem para {user['name']} sobre a importância da saúde financeira (máximo de 100 caractéres)"
            }
        ]
    )
    return completion.choices[0].message

for user in users:
    news = generate_ai_news(user)
    print(news)
    user['news'].append({
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": news
    })   