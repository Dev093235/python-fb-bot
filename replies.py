import random

# 1000+ Flirty Hinglish Replies (Example - Add More)
flirty_replies = [
    "Tum offline ho to bhi dil tumse baatein karta hai! 😉",
    "Agar cute hone ki competition hoti, to tum hamesha winner hoti! 😍",
    "Tumhari aankhon me aisa kya hai jo mujhe baar baar ghurta rehne pe majboor karta hai? 😘",
    "Jab tum likhti ho, lagta hai jaise koi angel type kar rahi ho! 😇",
    "Mujhse baat karke tum bore to nahi ho rahi na? 🤭",
    "Tum itni pyari ho ki Google bhi tumhe search karne lag jaaye! 😆",
    "Mujhe tumhari addiction ho gayi hai, koi rehab batao! 😜",
    "Tumhare bina chat ka maza hi nahi aata! 😏",
    "Tumhe dekhke lagta hai ki rab ne fursat se tumhe banaya hoga! ❤️",
    "Mujhe lagta hai tumhare dimples me mera dil kho gaya hai! 😍",
]

# Random Flirty Message Dene Wala Function
def get_flirty_reply():
    return random.choice(flirty_replies)

# Test
if __name__ == "__main__":
    print(get_flirty_reply())  # Random flirty message print karega
