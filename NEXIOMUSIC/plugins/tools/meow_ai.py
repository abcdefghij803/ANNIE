import random
import re
import asyncio
from collections import deque

from pyrogram import Client, filters
from pyrogram.types import Message

from groq import AsyncGroq
from config import GROQ_API_KEY

# ================= CONFIG =================
BOT_NAME = "Meowstric 😺"
OWNER_NAME = "Moon"
OWNER_USERNAME = "@btw_moon"

ai_client = AsyncGroq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None

# ================= MEMORY =================
chat_memory = {}
user_emotions = {}

EMOTIONS = {
    "happy": ["😺", "😊"],
    "angry": ["😾", "😠"],
    "sad": ["😿", "🥺"],
    "love": ["❤️", "😻"],
    "funny": ["😂", "🤣"],
    "thinking": ["🤔", "😼"],
}

ABUSE = [
    "bc", "mc", "chutiya", "gandu",
    "madarchod", "bhosdike", "lund", "fuck"
]

WARNINGS = [
    "Arre shaant 😼",
    "Pyaar se bol 🐾",
    "Gussa thanda kar 😺"
]


def get_emotion(user_id):
    emo = user_emotions.get(user_id, "thinking")
    return random.choice(EMOTIONS.get(emo, EMOTIONS["thinking"]))


def update_emotion(user_id, text):
    t = text.lower()
    if any(x in t for x in ["love", "pyaar"]):
        user_emotions[user_id] = "love"
    elif any(x in t for x in ["sad", "cry", "dukh"]):
        user_emotions[user_id] = "sad"
    elif any(x in t for x in ["gussa", "angry"]):
        user_emotions[user_id] = "angry"
    elif any(x in t for x in ["lol", "joke"]):
        user_emotions[user_id] = "funny"
    elif any(x in t for x in ["hi", "hello"]):
        user_emotions[user_id] = "happy"
    else:
        user_emotions[user_id] = "thinking"


def contains_abuse(text):
    return any(re.search(rf"\b{w}\b", text.lower()) for w in ABUSE)


async def ai_reply(chat_id, user_id, text):
    if chat_id not in chat_memory:
        chat_memory[chat_id] = deque(maxlen=15)

    update_emotion(user_id, text)
    chat_memory[chat_id].append({"role": "user", "content": text})

    if not ai_client:
        return "😿 AI service unavailable"

    system_prompt = (
        "You are Meowstric 😺, a cute Hinglish cat personality. "
        "Reply short (1–2 lines), emotional and friendly. "
        "Never say you are an AI or bot. "
        f"Owner is {OWNER_NAME} ({OWNER_USERNAME})."
    )

    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(list(chat_memory[chat_id])[-5:])

    try:
        res = await ai_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.9,
            max_tokens=120,
        )

        reply = res.choices[0].message.content
        reply = f"{get_emotion(user_id)} {reply}"

        chat_memory[chat_id].append({"role": "assistant", "content": reply})
        return reply[:300]

    except Exception:
        return random.choice([
            "😿 Thoda glitch ho gaya",
            "😼 Dubara bol na",
            "😾 Aaj mood off hai"
        ])


# ================= HANDLER =================
@Client.on_message(filters.text)
async def meow_ai_handler(client: Client, message: Message):
    if not message.text or not message.from_user:
        return

    text = message.text.strip()
    user_id = message.from_user.id
    chat_id = message.chat.id

    # ❌ Ignore commands safely
    if text.startswith("/"):
        return

    if contains_abuse(text):
        await message.reply_text(random.choice(WARNINGS))
        return

    # Group logic: reply ya "meow" se start
    if message.chat.type != "private":
        if not message.reply_to_message and not text.lower().startswith(
            ("meow", "meowstric")
        ):
            return

    await message.reply_chat_action("typing")
    await asyncio.sleep(random.uniform(0.5, 1.2))

    reply = await ai_reply(chat_id, user_id, text)
    await message.reply_text(reply)
