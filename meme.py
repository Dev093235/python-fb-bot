import random

def send_meme():
    memes = ["meme1.jpg", "meme2.jpg", "meme3.jpg"]
    return random.choice(memes)

if __name__ == "__main__":
    print("Sending meme:", send_meme())
