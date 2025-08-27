# botstatus.py
import time, psutil
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from NEXIOMUSIC import app  # Apke main bot ka client

# Start time for uptime
START_TIME = time.time()

# Bots + Assistants mapping
BOTS = {
    "@musicXanime_bot": "@musicXanime_assistant",
    "@Kitty_musicXbot": "@Kitty_assistant",
    "@mommy_xbot": "@mommy_assistant",
}


def get_sys_stats():
    """Return uptime, cpu, ram"""
    uptime = time.strftime("%Hh:%Mm:%Ss", time.gmtime(time.time() - START_TIME))
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    return uptime, cpu, ram


async def format_status():
    """Return attractive bot + assistant status message"""
    uptime, cpu, ram = get_sys_stats()

    blocks = []
    for bot, assistant in BOTS.items():
        # Bot check
        try:
            user = await app.get_users(bot)
            bot_status = "ᴧʟɪᴠє ✅" if user else "ᴅєᴀᴅ ❌"
        except Exception:
            bot_status = "ᴅєᴀᴅ ❌"

        # Assistant check
        try:
            user2 = await app.get_users(assistant)
            ass_status = "ᴧʟɪᴠє ✅" if user2 else "ᴅєᴀᴅ ❌"
        except Exception:
            ass_status = "ᴅєᴀᴅ ❌"

        blocks.append(
            f"╭⎋ {bot} : {bot_status}\n"
            f"├⊚ Assistant : {ass_status}\n"
            f"╰⊚ Uptime : {uptime} | CPU : {cpu}% | RAM : {ram}%\n"
        )

    text = f"""
**─────────────────────────
│ ᴡєʟᴄσϻє ᴛσ ˹ 𝐁ᴏᴛs˼ ʙσᴛ sᴛᴧᴛυs │
─────────────────────────
{''.join(blocks)}
─────────────────────────
⊚ ʟᴧsᴛ ᴄʜєᴄᴋєᴅ : {time.strftime("%d %b %Y %H:%M:%S")}
─────────────────────────
❍ 𝐏ᴏᴡєʀєᴅ 𝖡ʏ » Moon 🌙
─────────────────────────**
"""
    return text


@app.on_message(filters.command("botstatus"))
async def bot_status_cmd(client, message):
    """Command to show bot status"""
    text = await format_status()
    buttons = InlineKeyboardMarkup(
        [[InlineKeyboardButton("🔄 Refresh", callback_data="refresh_status")]]
    )
    await message.reply_text(text, reply_markup=buttons)


@app.on_callback_query(filters.regex("refresh_status"))
async def refresh_status_cb(client, callback_query):
    """Refresh button callback"""
    text = await format_status()
    buttons = InlineKeyboardMarkup(
        [[InlineKeyboardButton("🔄 Refresh", callback_data="refresh_status")]]
    )
    await callback_query.message.edit_text(text, reply_markup=buttons)
