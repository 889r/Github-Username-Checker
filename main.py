#Main
import random
import requests
import string
import os
import json
from telegram import Bot

#Logger / Colorama
import colorama
from colorama import Fore
from modules.logger import setup_logger

#-------------------------------------------------------

os.system("cls")
os.system("title Github Username Checker")

#start logger
logger = setup_logger()

#colorama.initialise
colorama.init()

async def send_req(name, bot, chat_id, debug):
    link = f"https://github.com/{name}"
    resp = requests.get(link)
    if resp.status_code == 404:
        logger.info(f"{name} : Username Available")
        with open("valid.txt", "a") as file:
            file.write(f"@{name} <- Available Username\n")
        if bot and chat_id:
            await bot.send_message(chat_id, f"@{name} <- Available Username / Github")
    elif resp.status_code == 200 and debug:
        logger.info(f"{name} : Username Taken")
    elif resp.status_code == 429 and debug:
        logger.warning(f"Rate limit exceeded for {name}")

async def main():
    length = int(input(f"[{Fore.CYAN}?{Fore.RESET}] Length of users u want to check >>> "))
    os.system("cls")
    
    # Read bot token and chat ID from config.json if available
    bot_token = None
    chat_id = None
    try:
        with open("config.json", "r") as config_file:
            config = json.load(config_file)
            bot_token = config.get("bot_token")
            chat_id = config.get("chat_id")
    except FileNotFoundError:
        logger.error("config.json file not found. Telegram notifications will be disabled.")

    if bot_token and chat_id:
        bot = Bot(token=bot_token)
    else:
        bot = None

    while True:
        name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
        await send_req(name, bot, chat_id, False)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
