from flask import Flask, request
import requests

# Flask app setup
app = Flask(__name__)

# Your Telegram bot token
BOT_TOKEN = '8105328463:AAEpq_gJIAalaq0UVQrsvXlARBrlQhxyqJ0'

# Telegram API URL
BASE_URL = f'https://api.telegram.org/bot{BOT_TOKEN}'

# Handle incoming webhook messages
@app.route('/', methods=['POST'])
def webhook():
    data = request.json

    # Parse incoming message
    chat_id = data['message']['chat']['id']
    text = data['message'].get('text', '')

    # Response logic
    if text == '/start':
        send_message(chat_id, "سلام من ربات امیر هستم، چه کاری از دستم برمیاد؟", buttons=[["سلام"], ["حالت چطوره؟"]])
    elif text == "سلام":
        send_message(chat_id, "حالت چطوره؟")
    elif text == "حالت چطوره؟":
        send_message(chat_id, "ممنون، تو چطوری؟")

    return "OK", 200

def send_message(chat_id, text, buttons=None):
    payload = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup': {
            'keyboard': buttons,
            'resize_keyboard': True,
            'one_time_keyboard': True
        } if buttons else None
    }
    requests.post(f'{BASE_URL}/sendMessage', json=payload)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
