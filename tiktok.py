import random
import time
import requests
import string
import sys
import logging
import os

os.system("cls")
os.system("title TikTok Username Checker")

# Check if the platform is Windows
if sys.platform.startswith('win'):
    import colorama
    colorama.init()

from colorama import Fore

# Configuring logging
logging.basicConfig(format=f"[{Fore.LIGHTBLACK_EX}%(asctime)s{Fore.RESET}] %(message)s", datefmt='%H:%M:%S', level=logging.INFO)
logger = logging.getLogger()

def send_req(name, debug):
    link = f"https://www.tiktok.com/@{name}"
    resp = requests.get(link)
    
    if "No user was found" in resp.text:
        logger.info(f"{name} : Username available")
        with open("tiktok-valid.txt", "a") as file:
            file.write(f"{name} <- Available Username  /  t.me/rei07x\n")
    elif resp.status_code == 200:
        logger.info(f"{name} : Username taken")
    elif resp.status_code == 429 and debug:
        logger.warning(f"Rate limit exceeded for {name}")

def main():
    length = int(input(f"[{Fore.CYAN}?{Fore.RESET}] Length of users you want to check >>> "))
    while True:
        name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
        send_req(name, False)

if __name__ == "__main__":
    main()
