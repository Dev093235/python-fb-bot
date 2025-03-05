import json
import random
import time
from fbchat import Client
from fbchat.models import Message
from replies import get_flirty_reply

# Cookies Load Karna
def load_cookies():
    with open("cookies.json", "r") as file:
        return json.load(file)

# Facebook Login with Cookies
cookies = load_cookies()
client = Client("", "", session_cookies=cookies)

print(f"Logged in as: {client.uid}")

# Auto-Reply Function
def auto_reply():
    while True:
        unread_messages = client.fetch_unread()
        for message in unread_messages:
            sender_id = message.author
            if sender_id != client.uid:  # Apne aap ko reply na kare
                reply = get_flirty_reply()
                client.send(Message(text=reply), thread_id=sender_id, thread_type=ThreadType.USER)
                print(f"Replied to {sender_id}: {reply}")
        
        time.sleep(5)  # 5 sec wait kare next check ke liye

# Start Bot
if __name__ == "__main__":
    auto_reply()
