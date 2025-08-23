import asyncio
import importlib
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from NEXIOMUSIC import LOGGER, app, userbot
from NEXIOMUSIC.core.call import SACHIN
from NEXIOMUSIC.misc import sudo
from NEXIOMUSIC.plugins import ALL_MODULES
from NEXIOMUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

# 🔹 Flask + yt_dlp
from flask import Flask, request, jsonify
import yt_dlp
import os
import threading

app_flask = Flask(__name__)
DOWNLOADS = "downloads"
os.makedirs(DOWNLOADS, exist_ok=True)

ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": os.path.join(DOWNLOADS, "%(id)s.%(ext)s"),
    "quiet": True,
    "no_warnings": True,
    "geo_bypass": True,
    "nocheckcertificate": True,
}

@app_flask.route("/download", methods=["GET"])
def download_audio():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "Missing ?url= param"}), 400
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
        return jsonify({
            "status": "ok",
            "title": info.get("title"),
            "file": os.path.abspath(filename)
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


def run_flask():
    app_flask.run(host="0.0.0.0", port=5000, debug=False)


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error(
            "❖ ASSISTANT  SESSION NOT FILLED, PLEASE FILL A PYROGRAM SESSION 💜"
        )
        exit()

    # Flask ko alag thread me run karenge
    threading.Thread(target=run_flask, daemon=True).start()
    LOGGER("NEXIOMUSIC").info("Flask API started on /download ✅")

    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass

    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("NEXIOMUSIC.plugins" + all_module)
    LOGGER("NEXIOMUSIC.plugins").info("❖ NEXIO MODULES LOADED 🤎")
    await userbot.start()
    await SACHIN.start()
    try:
        await SACHIN.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("NEXIOMUSIC").error(
            "❖ PLEASE TURN ON THE VOICE CHAT OF OUR LOGGER GROUP|CHANNEL NEXIO MUSIC STOPPED 🧡"
        )
        exit()
    except:
        pass
    await SACHIN.decorators()
    LOGGER("NEXIOMUSIC").info(
        "❖ Kishuu Music Bot Started Successfully 💜 (With Flask API)"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("NEXIOMUSIC").info("❖ STOPPING NEXIO MUSIC BOT 💛")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
