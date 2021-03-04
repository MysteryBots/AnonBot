# Anonymous Sender Bot
> A star ⭐ from you means a lot to us! 

<p align="center"><a href="https://www.github.com/MysteryBots/AnonBot"><img src="https://telegra.ph/file/1f46b268ce67b6300bb92.jpg" width="5000"></a></p>


Telegram bot to remove the forwarded tag from messages.

[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

<details open="open">
  <summary> Table of Contents</summary>
  <ol>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#deploy-to-heroku">Deploy To Heroku</a></li>
        <li><a href="#local-deploying">Local Deploying</a></li>
      </ul>
    </li>
    <li>
      <a href="#environment-variables">Environment Variables</a>
      <ul>
        <li><a href="#mandatory-vars">Mandatory Vars</a></li>
        <li><a href="#optional-vars">Optional Vars</a></li>
      </ul>
    </li>
    <li><a href="#functions">Functions</a></li>
    <li><a href="#to-do">To-Do</a></li>
    <li><a href="#stats">Stats</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#credits">Credits</a></li>
    <li><a href="#support">Support</a></li>
  </ol>
</details>


## Usage

### Deploy to Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/MysteryBots/AnonBot)

1) Tap on above button and fill `API_ID`, `API_HASH`, `BOT_TOKEN`. Alternatively fill `OWNER_ID` and `OWNER_NAME`. 
Note : Fill both or leave both unless bot won't work.
2) Then tap "Deploy App" below it. Wait till deploying is complete (will take atmost 2 minutes). 
3) After deploying is complete, tap on "Manage App"
4) Check the logs to see if your bot is ready! 

### Local Deploying
1) Clone the repo
   ```markdown
   git clone https://github.com/MysteryBots/AnonBot
   ```
2) Edit `Config.py` and fill the needed variables by following [this](https://github.com/MysteryBots/AnonBot/blob/master/Config.py#L11) 

3) Enter the directory
   ```markdown
   cd AnonBot
   ```
4) Run the file
   ```markdown
   python3 anonbot.py
   ```

## Environment Variables
#### Mandatory Vars
- `API_ID` - Get this from [my.telegram.org](https://my.telegram.org/auth) or [@TgOrgBot](https://t.me/TgOrgBot) 
- `API_HASH` - Get this from [my.telegram.org](https://my.telegram.org/auth) or [@TgOrgBot](https://t.me/TgOrgBot) 
- `BOT_TOKEN` - Get this from [@BotFather](https://t.me/BotFather) 
#### Optional Vars 
> (fill both or neither)
- `OWNER_ID` - Get it from [@MissMiley_bot](https://t.me/MissMiley_bot) by sending /id to it.
- `OWNER_NAME` - Your Name (to be shown as owner in bot)


## Functions
> More features soon, this is an minimal example :) 
1) Removes the tag for everything including texts, images, stickers, videos, inline messages, documents and even polls, location, etc. 
2) Support to remove caption if you don't need caption!! 
3) Specify owner's account to get help or something.

## To-Do
1) Add database to support Channel Posting easily
2) Add support to remove specific entities like Hashtags, URLs, etc. 
3) Support for bot stats in Telegram
4) Detect NSFW stuff to prevent take down of any bot.
5) Support for groups, message dump n banning

## Stats
[![GitHub forks](https://img.shields.io/github/forks/MysteryBots/AnonBot.svg?style=social&label=Fork&maxAge=2592000)](https://github.com/MysteryBots/AnonBot/network/) [![GitHub stars](https://img.shields.io/github/stars/MysteryBots/AnonBot.svg?style=social&label=Star&maxAge=2592000)](https://github.com/MysteryBots/AnonBot/stargazers/) [![GitHub watchers](https://img.shields.io/github/watchers/MysteryBots/AnonBot.js.svg?style=social&label=Watch&maxAge=2592000)](https://github.com/MysteryBots/AnonBot/watchers/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/MysteryBots/AnonBot/graphs/commit-activity)



## License
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)


## Contributing
[![GitHub contributors](https://img.shields.io/github/contributors/MysteryBots/AnonBot.svg)](https://github.com/MysteryBots/AnonBot/graphs/contributors/)
> Contributions are heartily accepted. 

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

## Credits
[Dan Tès](https://github.com/delivrance) for his [Pyrogram](https://docs.pyrogram.org) Library

## Support
Channel :- [@MysteryBots](https://t.me/MysteryBots)

Group Chat :- [@MysteryBotsChat](https://t.me/MysteryBotsChat)

## :) 

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/MysteryBots) 

[![ForTheBadge makes-people-smile](http://ForTheBadge.com/images/badges/makes-people-smile.svg)](https://github.com/MysteryBots)


