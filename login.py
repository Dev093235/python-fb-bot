import requests
import json

# Cookies file read karna
def load_cookies():
    with open("cookies.json", "r") as file:
        return {cookie["name"]: cookie["value"] for cookie in json.load(file)}

# Facebook pe login check karna
def check_login():
    cookies = load_cookies()
    url = "https://m.facebook.com/home.php"  # Facebook ka homepage

    response = requests.get(url, cookies=cookies)
    
    if "home_icon" in response.text or "notifications_jewel" in response.text:
        print("[✅] Login Successful!")
        return True
    else:
        print("[❌] Login Failed! Cookies Expired.")
        return False

if __name__ == "__main__":
    check_login()
