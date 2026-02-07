from pyrogram import filters
from pyrogram.types import Message

from NEXIOMUSIC import app
from NEXIOMUSIC.misc import BANNED_USERS
from groq import AsyncGroq
import os
from collections import deque

# ========= CONFIG =========
GROQ_API_KEY = os.getenv("GROQ_API_KEY","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")
client = AsyncGroq(api_key=GROQ_API_KEY)

# ========= MEMORY =========
# chat_id: deque
CHAT_MEMORY = {}

# ========= AI FUNCTION =========
async def get_ai_reply(chat_id: int, text: str) -> str:
    if chat_id not in CHAT_MEMORY:
        CHAT_MEMORY[chat_id] = deque(maxlen=10)

    CHAT_MEMORY[chat_id].append({"role": "user", "content": text})

    messages = [
        {
            "role": "system",
            "content": (
                "You are a friendly Hinglish chatbot. "
                "Talk like a real human friend. "
                "Use emojis 😊🔥😂. "
                "Keep replies short and natural."
            )
        }
    ]

    messages.extend(CHAT_MEMORY[chat_id])

    try:
        res = await client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.9,
            max_tokens=150,
        )
        reply = res.choices[0].message.content
        CHAT_MEMORY[chat_id].append({"role": "assistant", "content": reply})
        return reply
    except Exception:
        return "😅 Thoda sa issue aa gaya, phir try karna yaar!"

# ========= COMMAND CHAT =========
@app.on_message(
    filters.command("chat") & filters.group & ~BANNED_USERS
)
async def chat_command(client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text(
            "🗨️ Use: `/chat hello bot`",
            quote=True
        )

    text = message.text.split(None, 1)[1]
    await message.reply_chat_action("typing")

    reply = await get_ai_reply(message.chat.id, text)
    await message.reply_text(reply, quote=True)

# ========= REPLY CHAT =========
@app.on_message(
    filters.reply & filters.group & ~BANNED_USERS
)
async def reply_chat(client, message: Message):
    if not message.reply_to_message.from_user:
        return

    if message.reply_to_message.from_user.id != app.id:
        return

    await message.reply_chat_action("typing")
    reply = await get_ai_reply(message.chat.id, message.text)
    await message.reply_text(reply, quote=True)

# ========= CLEAR MEMORY =========
@app.on_message(
    filters.command("clearchat") & filters.group & ~BANNED_USERS
)
async def clear_chat(client, message: Message):
    CHAT_MEMORY.pop(message.chat.id, None)
    await message.reply_text("🧹 Chat memory clear ho gayi! Fresh start 😌")
