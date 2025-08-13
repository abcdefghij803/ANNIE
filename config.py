import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# ❖ LOAD ENVIRONMENT VARIABLES FROM . ENV FILE 
load_dotenv()

# ❖ TELEGRAM API CREDENTIALS - GET THESE FROM THE TELEGRAM API WEBSITE 
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")

# ❖ SPECIFY WHERE TO GET THE FOLLOWING CREDENTIALS 
OWNER_USERNAME = getenv("OWNER_USERNAME", "moon_m_5")
BOT_USERNAME = getenv("BOT_USERNAME", "musicXanime_bot")
BOT_NAME = getenv("BOT_NAME", "Annie 𐌑ᥙsiᥴ [ ɴᴏ ᴀᴅʂ ] 🕊")
ASSUSERNAME = getenv("ASSUSERNAME", "AnnieMusicPlayarx")
EVALOP = list(map(int, getenv("EVALOP", "").split()))
MONGO_DB_URI = getenv("MONGO_DB_URI", None)
LOGGER_ID = int(getenv("LOGGER_ID", ""))
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

# ❖ EXTERNAL APIs - GET THESE FROM THEIR RESPECTIVE PROVIDERS 
GPT_API = getenv("GPT_API", "")
PLAYHT_API = getenv("PLAYHT_API", "")
OWNER_ID = int(getenv("OWNER_ID", "7789325573"))

# ❖ HEROKU DEPLOYMENT SETTINGS - REFER TO HEROKU DOCUMENTATION ON HOW TO OBTAIN THESE 
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/abcdefghij803/ANNIE")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# ❖ SUPPORT AND CONTACT INFORMATION - PROVIDE YOUR OWN SUPPORT CHANNELS 
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/btw_moon")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+zOo21P9qDW4wZjk1")

API_URL = getenv("API_URL", 'https://api.thequickearn.xyz') #youtube song url
VIDEO_API_URL = getenv("VIDEO_API_URL", 'https://api.video.thequickearn.xyz')
API_KEY = getenv("API_KEY", 'AIzaSyA_a1fqULooB8286h2XBXYp942edxz7zaM') # youtube song api key

# ❖ SERVER LIMITS AND CONFIGURATIONS - THESE CAN BE SET BASED ON YOUR SERVER CONFIGURATIONS 
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "2500"))
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))

# ❖ EXTERNAL SERVICE CREDENTIALS - OBTAIN THESE FROM SPOTIFY 
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "22b6125bfe224587b722d6815002db2b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c9c63c6fbf2f467c8bc68624851e9773")

# ❖ TELEGRAM FILE SIZE LIMITS - SET THESE ACCORDING TO YOUR REQUIREMENTS 
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

# ❖ PYROGRAM SESSION STRINGS - YOU NEED TO GENERATE THESE YOURSELF 
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


STICKER = [
    "CAACAgUAAxkBAAEBWPdm5mPQY_ZkO0ubAVCfrLsQrQ72JQACjAkAArIJGVUWyBghZ-dV-x4E",
    "CAACAgUAAxkBAAEBWPhm5mPYKcuczEfuCEOMirtaXp-1dwAC4QoAAq16GFWaCSi4wwAB_FgeBA",
    "CAACAgUAAxkBAAEBWPlm5mPeoSKNaQG_6nnQu-QDS3G9MAACSggAAq3yEVUPJy8Z5F0c4B4E",
    "CAACAgUAAxkBAAEBWPpm5mPj0JHkFNtPWwF06LYel6I6bAACNwgAAjdAGFXRuQTa8apeoB4E",
    "CAACAgUAAxkBAAEBWPtm5mPpBAgyaU64RhnCRrMi2N3scgACEQgAAhUSGVUMJ-alW9VubB4E",
    "CAACAgUAAxkBAAEBWPxm5mP25bpfq3-MphrBt7_QsuXLlAACqQoAAnmvGFWxfDyUI6qURR4E",
    "CAACAgUAAxkBAAEBWP1m5mP-nQ-yfPDVY_DtmjJKnKFqTwACHgoAAsmuGVVnKBvEVZZMvB4E",
    "CAACAgUAAxkBAAEBWP5m5mQPxhxaKOaG5xJgUy14_BSBbAACfQkAAghYGFVtSkRZ5FZQXB4E", 
]


START_IMG_URL = [
    "https://telegra.ph/file/8fb11f38033d3195c9c8c.jpg",
    "https://telegra.ph/file/106167c80a3fc3ab9f1e8.jpg",
    "https://telegra.ph/file/89070543c0f7f2e51118d.jpg",
    "https://telegra.ph/file/3a0afc7a07f35747684eb.jpg",
    "https://telegra.ph/file/0db46c5fca2c69829a7d4.jpg",
    "https://telegra.ph/file/f7e5522656c24abf1bd90.jpg",
    "https://telegra.ph/file/621f76810deb42513f345.jpg",
    "https://telegra.ph/file/095d4d1a638bd42e54189.jpg",
    "https://telegra.ph/file/0a6cf2af7eead7fcb0745.jpg",
]

PING_VID_URL = getenv(
    "PING_VID_URL", "https://graph.org/file/babb71b593f36549218ce.jpg"
    )

PLAYLIST_IMG_URL = "https://graph.org/file/4a254d425fb4bf09b7470.jpg"

STATS_VID_URL = "https://graph.org/file/51f37e3c2d4aaff5cf80e.jpg"

TELEGRAM_AUDIO_URL = "https://graph.org/file/df01978f91c14b16292f1.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/a6e3e9d54c8b2e01787b6.jpg"

STREAM_IMG_URL = "https://graph.org/file/49bcbc23be713fbe06bac.jpg"

SOUNCLOUD_IMG_URL = "https://graph.org/file/809651f9be99ee2bf76ab.jpg"

YOUTUBE_IMG_URL = "https://graph.org/file/134c9f52f4ba0f7691cd1.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/4b5c2174d7f38b4b4abd7.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/80feff5bb4a03cf331945.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/0379defeb51910065beac.jpg"

FAILED = "https://graph.org/file/323b07bccd5e5e1f81f61.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - YOUR SUPPORT_CHANNEL URL IS WRONG. PLEASE ENSURE THAT IT STARTS WITH https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - YOUR SUPPORT_CHAT URL IS WRONG. PLEASE ENSURE THAT IT STARTS WITH https://"
        )
