from anonbot import app
from Config import Config
from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = "Hey {}. \n\nWelcome to {} \n\nSend me anything and I'll send it back after removing the forwarded tag"

    if Config.OWNER_ID != 0:
        if Config.OWNER_NAME:
            START += (
                f"\n\nMy Owner :- [{Config.OWNER_NAME}](tg://user?id={Config.OWNER_ID})"
            )
        else:
            print(
                "You added OWNER_ID but not OWNER_NAME. You need to put both or neithers"
            )
            print("Quitting the bot")
            raise SystemExit
    else:
        START += f"\n\nBy @MysteryBots ♥"

    # About Message
    ABOUT = "**About This Bot** \n\nThis is an open source forwarded tag remover bot by @MysteryBots \n\nSource : [Click Here](https://github.com/MysteryBots/AnonBot) \n\nFramework : [Pyrogram](docs.pyrogram.org) \n\nLanguage : [Python](www.python.org) \n\nDeveloper : [Mყʂƚҽɾყ Bσყ](https://t.me/MysteryxD)"

    if Config.OWNER_ID != 0:
        if Config.OWNER_NAME:
            ABOUT += (
                f"\n\nMy Owner :- [{Config.OWNER_NAME}](tg://user?id={Config.OWNER_ID})"
            )
        else:
            print(
                "You added OWNER_ID but not OWNER_NAME. You need to put both or neither"
            )
            print("Quitting the bot")
            raise SystemExit

	# Deploy Message
    DEPLOY = '**Wanna create your own such bot??** \n\nThis is simple and open source bot. \nJust click below on source code and tap on "Deploy to Heroku" to create your own bot. \n\nClick Here for [Source Code](https://github.com/MysteryBots/AnonBot)'

    # Home Button
    home_button = [[InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]]

    # Remove Caption Button
    remove_button = [InlineKeyboardButton("� Remove Caption �", callback_data="remove")]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("🎪 About 🎪", callback_data="about"),
            InlineKeyboardButton("Create your own", callback_data="deploy"),
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/MysteryBots")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/MysteryBotsChat")],
    ]
