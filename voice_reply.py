import os
import random
import gtts
from fbchat import Client
from fbchat.models import Message, MessageAttachment

# Voice Reply Folder
VOICE_FOLDER = "voices/"

# Function: Hindi Voice Reply Generate Karna
def generate_voice_reply(text):
    filename = f"{VOICE_FOLDER}reply_{random.randint(1000,9999)}.mp3"
    tts = gtts.gTTS(text, lang="hi")
    tts.save(filename)
    return filename

# Function: Voice Reply Send Karna
def send_voice_reply(thread_id, text):
    voice_path = generate_voice_reply(text)
    if voice_path:
        client.sendLocalFiles(voice_path, message=Message(text="🎤 Suno bhai..."), thread_id=thread_id, thread_type=ThreadType.USER)
        print(f"Voice Reply Sent to {thread_id}: {voice_path}")
        os.remove(voice_path)  # Delete File After Sending
    else:
        print("Voice Reply Generation Failed!")

# Start Voice Reply Bot
if __name__ == "__main__":
    from main import client  # Login from main.py
    target_user = input("Enter User ID to send voice reply: ")
    reply_text = input("Enter Reply Text: ")
    send_voice_reply(target_user, reply_text)
