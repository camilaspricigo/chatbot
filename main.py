import sys
import time
import telepot
import json
from telepot.loop import MessageLoop

with open("token.json", "r") as f:
  TOKEN = json.load(f)
  

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id, msg['text'])


bot = telepot.Bot(TOKEN["token_telegram"])
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)