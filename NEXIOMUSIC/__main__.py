import asyncio
import importlib
import os
from flask import Flask, request, jsonify
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall
import yt_dlp

import config
from NEXIOMUSIC import LOGGER, app, userbot
from NEXIOMUSIC.core.call import SACHIN
from NEXIOMUSIC.misc import sudo
from NEXIOMUSIC.plugins import ALL_MODULES
from NEXIOMUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


# ------------------- Flask API -------------------
flask_app = Flask(__name__)

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


@flask_app.route("/download", methods=["GET"])
def download():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "URL required"}), 400

    try:
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": f"{DOWNLOAD_DIR}/%(id)s.%(ext)s",
            "quiet": True,
            "no_warnings": True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)

        return jsonify({"path": os.path.abspath(file_path)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ------------------- Bot Init -------------------
async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("❖ ASSISTANT SESSION NOT FILLED ❖")
        exit()

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

    LOGGER("NEXIOMUSIC.plugins").info("❖ MODULES LOADED")

    await userbot.start()
    await SACHIN.start()

    try:
        await SACHIN.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("NEXIOMUSIC").error("❖ START A VC IN LOGGER GROUP ❖")
        exit()
    except:
        pass

    await SACHIN.decorators()
    LOGGER("NEXIOMUSIC").info("❖ BOT STARTED SUCCESSFULLY ❖")

    await idle()

    await app.stop()
    await userbot.stop()
    LOGGER("NEXIOMUSIC").info("❖ BOT STOPPED ❖")


if __name__ == "__main__":
    # Run Flask server in background
    loop = asyncio.get_event_loop()
    loop.create_task(loop.run_in_executor(None, flask_app.run, "0.0.0.0", 5000))

    # Run Music Bot
    loop.run_until_complete(init())
