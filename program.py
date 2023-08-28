import pandas as pd
import requests


# VARIÁVEIS ÚTEIS PARA O PROGRAMA
data_frame = pd.read_csv('data/SBP2023.csv')
user_ids  = data_frame['UserID'].tolist()
api_url = 'https://64e7b5e1b0fd9648b7904675.mockapi.io'

# FUNÇÃO PARA BUSCAR UM USUÁRIO POR ID
def get_user(id):
    response = requests.get(f'{api_url}/etl/{id}')
    return response.json() if response.status_code == 200 else None

# LISTA DE USUÁRIOS ATRAVÉS DOS IDS CONTIDOS NO ARQUIVO
users = [user for id in user_ids if (user := get_user(id)) is not None]

# UM SIMPLES FOR PELOS USUÁRIOS PARA CHECAR SE ESTÁ CORRETO
for user in users:
    print(user)

# FUNÇÃO PARA ALTERAR O E-MAIL ATRAVÉS DO ID
def change_user_mail(id, mail):
    user = get_user(id)
    user['mail'] = mail
    requests.put(f"{api_url}/etl/{user['id']}", json=user)

# MENU INTERATIVO PARA ALTERAÇÃO UTILIZANDO A FUNÇÃO
while True :
    print("Users registereds in list: ")
    for user in users:
        print(user['id'])

    user_id = input("Inser user ID to change: ")
    new_mail = input("Insert a new mail address: ")

    change_user_mail(user_id, new_mail)

    print("### UPDATED ###")
    print(get_user(user_id))

    choice = input("Continue changing user´s mail address? 0 - NO // 1 - YES ")
    if choice == "0":
        break


