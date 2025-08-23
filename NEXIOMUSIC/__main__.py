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


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("❖ ASSISTANT  SESSION NOT FILLED, PLEASE FILL A PYROGRAM SESSION 💜")
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
    LOGGER("NEXIOMUSIC.plugins").info("❖ NEXIO MODULES LOADED 🤎")
    await userbot.start()
    await SACHIN.start()
    try:
        await SACHIN.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("NEXIOMUSIC").error(
            "❖ PLEASE TRUN ON THE VOICE CHAT OF OUR LOGGER GROUP|CHANNEL NEXIO MUAIC STOPPED 🧡"
        )
        exit()
    except:
        pass
    await SACHIN.decorators()
    LOGGER("NEXIOMUSIC").info(
        "\x4b\x69\x73\x68\x75\x20\x4d\x75\x73\x69\x63\x20\x42\x6f\x74\x20\x53\x74\x61\x72\x74\x65\x64\x20\x53\x75\x63\x63\x65\x73\x73\x66\x75\x6c\x6c\x79\x2e"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("NEXIOMUSIC").info("❖ STOPING NEXIO MUAIC BOT 💛")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
