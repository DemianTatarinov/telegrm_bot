import requests

TOKEN = '7810257621:AAGJaCdniU-1bphCkXV2wNFr-pJtIyqXBO8'
URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

response = requests.get(URL)
data = response.json()

if 'result' in data and len(data['result']) > 0:
    chat_id = data['result'][0]['message']['chat']['id']
    print(f"Ваш chat_id: {chat_id}")
else:
    print("Не удалось получить chat_id. Отправьте сообщение вашему боту и запустите скрипт снова.")
