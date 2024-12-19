import os
from flask import Flask, request
import requests

# Flask app setup
app = Flask(__name__)

# Bot token from environment variable
BOT_TOKEN = os.environ.get("BOT_TOKEN")
if BOT_TOKEN is None:
    print("Error: BOT_TOKEN environment variable not set!")
    exit(1)

# Telegram API URL (base without specific endpoint)
BASE_URL = f'https://api.telegram.org/bot{BOT_TOKEN}'
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

bot = #Initialize your bot here

try:
    r = requests.get(f'{BASE_URL}/setWebhook?url={WEBHOOK_URL}')
    print(r.text) #Print result of setWebhook
    print("Webhook set successfully")
except requests.exceptions.RequestException as e:
    print(f"Error setting webhook: {e}")

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
  # Use environment variable for WEBHOOK_URL (set on Render)
  url = f'{BASE_URL}{BOT_TOKEN}/sendMessage'
  requests.post(url, json=payload)

if __name__ == '__main__':
  # Use environment variable PORT provided by Render (if available)
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)
