import time
from facebook_bot import FacebookBot

if __name__ == "__main__":
    bot = FacebookBot("cookies.json")
    bot.run()
