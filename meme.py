import os
import random
from fbchat import Client
from fbchat.models import Message, MessageAttachment

# Meme Folder Path
MEME_FOLDER = "memes/"

# Function: Random Meme Select Karna
def get_random_meme():
    memes = [m for m in os.listdir(MEME_FOLDER) if m.endswith((".jpg", ".png", ".gif"))]
    return os.path.join(MEME_FOLDER, random.choice(memes)) if memes else None

# Meme Send Karna
def send_meme(thread_id):
    meme_path = get_random_meme()
    if meme_path:
        client.sendLocalImage(meme_path, thread_id=thread_id, thread_type=ThreadType.USER)
        print(f"Meme Sent to {thread_id}: {meme_path}")
    else:
        print("No memes found!")

# Start Meme Sender
if __name__ == "__main__":
    from main import client  # Login from main.py
    target_user = input("Enter User ID to send meme: ")
    send_meme(target_user)
