import pyttsx3

def voice_reply(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    voice_reply("Hello! This is a voice reply bot.")
