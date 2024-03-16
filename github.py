import random
import time
import requests
import string
import sys
import logging
import os
from colorama import Fore

os.system("cls")
os.system("title Github Username Checker")

# Check if the platform is Windows
if sys.platform.startswith('win'):
    import colorama
    colorama.init()

# Configuring logging
logging.basicConfig(format=f"[{Fore.LIGHTBLACK_EX}%(asctime)s{Fore.RESET}] %(message)s", datefmt='%H:%M:%S', level=logging.INFO)
logger = logging.getLogger()

def send_req(name, debug):
    link = f"https://github.com/{name}"
    resp = requests.get(link)
    if resp.status_code == 404:
        logger.info(f"{name} : Username Available")
        with open("github-valid.txt", "a") as file:
            file.write(f"@{name} <- Available Username  /  t.me/rei07x\n")
    elif resp.status_code == 200 and debug:
        logger.info(f"{name} : Username Taken")
    elif resp.status_code == 429 and debug:
        logger.warning(f"Rate limit exceeded for {name}")

def main():
    length = int(input(f"[{Fore.CYAN}?{Fore.RESET}] Length of users u want to check >>> "))
    print()
    while True:
        name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
        send_req(name, False)

if __name__ == "__main__":
    main()
