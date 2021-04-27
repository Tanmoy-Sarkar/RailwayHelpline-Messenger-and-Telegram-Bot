# RailwayHelpline Messenger and Telegram Bot
![PyPI - Downloads](https://img.shields.io/pypi/dd/wit?label=Wit)
![PyPI - Downloads](https://img.shields.io/pypi/dd/tabulate?label=Tabulate)
![PyPI - Downloads](https://img.shields.io/pypi/dd/configparser?label=Tabulate)
![PyPI - Downloads](https://img.shields.io/pypi/dd/flask?label=Flask)
![PyPI - Downloads](https://img.shields.io/pypi/dd/pymessenger?label=Pymessenger)

### Live Bot Demo in Telegram <a href="http://t.me/Bangladesh_Railway_Helpline_Bot"> Railway Helpline </a>

## What the bot does?
This is a messenger bot for giving information related to the Railway Service (Rajshahi only) At present you can only ask about buying tickets/schedule/location of trains (more will be added) For Natural Language Processing Wit.ai was used. App is made with Python Flask Framework It is deployed in Heroku. Messenger: The page can be found at https://www.facebook.com/BangladeshRailwayHelpline/ Due to facebook permission problem bot cannot send message publicly. Telegram: Bot can be found at http://t.me/Bangladesh_Railway_Helpline_Bot

## Get code
```bash
git clone https://github.com/Tanmoy-Sarkar/RailwayHelpline-Messenger-and-Telegram-Bot.git
```
## Get Wit Access Token
Go to <a href="https://wit.ai/">Wit</a> make a account and get the access token

## Messenger Bot

### Creating Bot
Make a page in facebook and copy the FB access token and change the FB_ACCESS_TOKEN variable from the code
Set up webhook (can follow <a href="https://www.youtube.com/watch?v=sskRz_lsY8g&list=PLyb_C2HpOQSC4M3lzzrql7DSppTeAxh-x&index=3"> Here </a>)


### Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install flask,pymessenger,wit,requests.

```bash
pip install flask wit pymessenger requests
```

## Usage

Go to the "Messenger" directory

Run from the command line
```bash
python app.py
```

## Telegram Bot
## License
[MIT](https://choosealicense.com/licenses/mit/)

