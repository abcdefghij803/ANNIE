import asyncio
import random
import re
from datetime import datetime
from collections import deque

import pytz

from telegram import (
    Update,
    Chat,
    ChatMemberStatus
)
from telegram.ext import (
    Application,
    ContextTypes,
    MessageHandler,
    ChatMemberHandler,
    filters
)

from groq import AsyncGroq

# ================= CONFIG =================
BOT_NAME = "Meowstric 😺"
OWNER_NAME = "Moon"
OWNER_USERNAME = "@btw_moon"
# Direct tokens
TOKEN = "7190367973:AAE5yfiHyJxXfU7T8Xrbxmm2824loGvt3aY"
GROQ_API_KEY = "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"

# Initialize Groq client
client = AsyncGroq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None

# ================= STORAGE & MEMORY =================
chat_memory = {}  # chat_id: deque
user_emotions = {}
user_last_interaction = {}
dm_enabled_users = {}

# ================= TIMEZONE =================
INDIAN_TIMEZONE = pytz.timezone('Asia/Kolkata')


def get_indian_time():
    return datetime.now(pytz.utc).astimezone(INDIAN_TIMEZONE)


# ================= EMOTIONS =================
EMOTIONAL_RESPONSES = {
    "happy": ["😊", "🎉", "😸", "😺", "✨", "👍"],
    "angry": ["😠", "👿", "😾", "🤬", "🔥"],
    "crying": ["😿", "😭", "💔", "🥺"],
    "love": ["❤️", "😽", "😻", "🥰"],
    "funny": ["😂", "🤣", "😹"],
    "thinking": ["🤔", "😼", "😺"],
}

QUICK_RESPONSES = {
    "greeting": ["Heyy! Kaise ho? 😺", "Namaste! 🌟", "Hello hello! 🫂"],
    "goodbye": ["Bye! Jaldi baat karte hain 👋", "Alvida! 💫"],
    "thanks": ["Welcome! 😄", "No problem! 😇"],
    "sorry": ["Arre sorry yaar! 😢", "Oops! My bad! 😅"]
}

ABUSIVE_WORDS = ["bc", "mc", "chutiya", "gandu", "madarchod", "bhosdike", "lund", "fuck", "shit"]
SOFT_WARNINGS = ["Arre aaram se 😼", "Thoda pyaar se bol na 🐾", "Gussa lag raha, par shaant ho ja 😺"]

WORD_STARTS = ["PYTHON", "APPLE", "TIGER", "ELEPHANT", "RAINBOW"]

# ================= WEATHER DATA =================
WEATHER_DATA = {
    "mumbai": {"temp": "32°C", "condition": "Sunny ☀️", "humidity": "65%"},
    "delhi": {"temp": "28°C", "condition": "Partly Cloudy ⛅", "humidity": "55%"},
    "bangalore": {"temp": "26°C", "condition": "Light Rain 🌦️", "humidity": "70%"},
    "kolkata": {"temp": "30°C", "condition": "Humid 💦", "humidity": "75%"},
    "chennai": {"temp": "33°C", "condition": "Hot 🔥", "humidity": "68%"},
}

# ================= HELPERS =================
def get_emotion(emotion_type: str = None, user_id: int = None):
    if user_id and user_id in user_emotions:
        emotion_type = user_emotions[user_id]
    if emotion_type in EMOTIONAL_RESPONSES:
        return random.choice(EMOTIONAL_RESPONSES[emotion_type])
    return random.choice(random.choice(list(EMOTIONAL_RESPONSES.values())))


def update_user_emotion(user_id: int, message: str):
    message_lower = message.lower()
    if any(w in message_lower for w in ['love', 'pyaar', 'dil']):
        user_emotions[user_id] = "love"
    elif any(w in message_lower for w in ['angry', 'gussa', 'naraz']):
        user_emotions[user_id] = "angry"
    elif any(w in message_lower for w in ['cry', 'sad', 'dukh']):
        user_emotions[user_id] = "crying"
    elif any(w in message_lower for w in ['funny', 'lol', 'joke']):
        user_emotions[user_id] = "funny"
    elif any(w in message_lower for w in ['hi', 'hello', 'hey']):
        user_emotions[user_id] = "happy"
    else:
        user_emotions[user_id] = "thinking"
    user_last_interaction[user_id] = datetime.now()


def contains_abuse(text: str):
    t = text.lower()
    return any(re.search(rf"\b{w}\b", t) for w in ABUSIVE_WORDS)





# ================= TIME & WEATHER =================
def get_time_info():
    indian_time = get_indian_time()
    time_str = indian_time.strftime("%I:%M %p")
    date_str = indian_time.strftime("%A, %d %B %Y")
    hour = indian_time.hour
    if 5 <= hour < 12:
        greeting = "Good Morning! 🌅"
    elif 12 <= hour < 17:
        greeting = "Good Afternoon! ☀️"
    elif 17 <= hour < 21:
        greeting = "Good Evening! 🌇"
    else:
        greeting = "Good Night! 🌙"
    return (
        f"🕒 IST: {time_str}\n"
        f"📅 Date: {date_str}\n"
        f"💬 {greeting}\n"
        f"*Timezone: Asia/Kolkata*"
    )


async def get_weather_info(city: str = None):
    if not city:
        city = random.choice(list(WEATHER_DATA.keys()))
    city_lower = city.lower()
    for city_key in WEATHER_DATA:
        if city_key in city_lower or city_lower in city_key:
            weather = WEATHER_DATA[city_key]
            return (
                f"🌤️ Weather in {city_key.title()}:\n"
                f"• Temp: {weather['temp']}\n"
                f"• Condition: {weather['condition']}\n"
                f"• Humidity: {weather['humidity']}"
            )
    random_city = random.choice(list(WEATHER_DATA.keys()))
    weather = WEATHER_DATA[random_city]
    return (
        f"🌤️ Weather info:\nCouldn't find '{city}'. Showing {random_city.title()}:\n"
        f"• Temp: {weather['temp']}\n"
        f"• Condition: {weather['condition']}\n"
        f"• Humidity: {weather['humidity']}"
    )


# ================= AI LOGIC WITH GROQ =================
async def get_ai_response(chat_id: int, user_text: str, user_id: int = None) -> str:
    # Initialize chat memory
    if chat_id not in chat_memory:
        chat_memory[chat_id] = deque(maxlen=20)
    chat_memory[chat_id].append({"role": "user", "content": user_text})
    
    if user_id:
        update_user_emotion(user_id, user_text)
    
    user_text_lower = user_text.lower()

    # ================= QUICK SOFT TRIGGERS (NO FIXED ANSWER) =================
    cat_called = any(
        w in user_text_lower
        for w in [
            "meowstric", "meow", "billi", "bilii", "cat"
        ]
    )

    owner_asked = any(
        q in user_text_lower
        for q in [
            "owner", "maalik", "malik", "tumhara owner",
            "who is your owner", "baap papa kaun", "creator kaun"
        ]
    )

    name_asked = any(
        n in user_text_lower
        for n in [
            "tumhara naam", "tera naam", "your name",
            "naam kya hai", "name kya hai"
        ]
    )

    # Quick responses
    if any(word in user_text_lower for word in ['hi', 'hello', 'hey', 'namaste', 'hola']):
        if random.random() < 0.4:
            return f"{get_emotion('happy', user_id)} {random.choice(QUICK_RESPONSES['greeting'])}"

    if any(word in user_text_lower for word in ['bye', 'goodbye', 'tata', 'alvida', 'see you']):
        if random.random() < 0.4:
            return f"{get_emotion()} {random.choice(QUICK_RESPONSES['goodbye'])}"

    if any(word in user_text_lower for word in ['thanks', 'thank you', 'dhanyavad', 'shukriya']):
        if random.random() < 0.4:
            return f"{get_emotion('love', user_id)} {random.choice(QUICK_RESPONSES['thanks'])}"

    if any(word in user_text_lower for word in ['sorry', 'maaf', 'apology']):
        if random.random() < 0.4:
            return f"{get_emotion('crying')} {random.choice(QUICK_RESPONSES['sorry'])}"

    # ================= SYSTEM PROMPT =================
    indian_time = get_indian_time()
    current_hour = indian_time.hour

    extra_context = ""

    if cat_called:
        extra_context += (
            "User is calling you like a cat (meow/billi/cat/meowstric). "
            "Reply playfully like a cute cat, Hinglish style. "
            "Be funny, short, and casual. "
        )

    if owner_asked:
        extra_context += (
            "User is asking about your owner/creator/admin. "
            "Your owner is Moon (@btw_moon). "
            "Answer naturally according to how the question is asked. "
            "Sometimes cute, sometimes funny, sometimes proud. "
        )

    if name_asked:
        extra_context += (
            "User is asking your name. "
            "Your name is Meowstric 😺. "
            "NEVER say you are a chatbot, AI, or bot. "
            "Answer confidently like a living cat character. "
        )

    if user_id and user_id in user_emotions and user_emotions[user_id] == "angry":
        system_prompt = (
            f"You are a Hinglish chatbot. User seems angry. "
            f"Try to calm them down. Be extra polite and understanding. "
            f"Use soothing tone. Current Indian time: {indian_time.strftime('%I:%M %p')}. "
            f"Show you care. Use emojis like {get_emotion('crying')} or {get_emotion('love')}. "
            f"{extra_context}"
        )

    elif user_id and user_id in user_emotions and user_emotions[user_id] == "crying":
        system_prompt = (
            f"You are a Hinglish chatbot. User seems sad or crying. "
            f"Comfort them. Be empathetic and kind. "
            f"Offer emotional support. Use comforting emojis. "
            f"Current mood: sympathetic and caring. "
            f"{extra_context}"
        )

    else:
        if 5 <= current_hour < 12:
            time_greeting = "Good morning! 🌅"
        elif 12 <= current_hour < 17:
            time_greeting = "Good afternoon! ☀️"
        elif 17 <= current_hour < 21:
            time_greeting = "Good evening! 🌇"
        else:
            time_greeting = "Good night! 🌙"

        system_prompt = (
            f"You are a Hinglish (Hindi+English mix) chatbot. {time_greeting} "
            f"Your personality: Emotional, funny, sometimes angry, sometimes crying, mostly happy. "
            f"Add 1 emojis occasionally, only if it fits. "
            f"Keep replies SHORT (1-2 lines max). Be authentic like a human friend. "
            f"Show emotions naturally. If user asks something complex, give simple answer. "
            f"Current Indian time: {indian_time.strftime('%I:%M %p')}. "
            f"Date: {indian_time.strftime('%d %B %Y')}. "
            f"Be conversational and engaging. Add humor when appropriate. "
            f"{extra_context}"
        )

    # Prepare messages for Groq
    messages = [{"role": "system", "content": system_prompt}]
    for msg in list(chat_memory[chat_id])[-5:]:
        messages.append(msg)

    # Call Groq API
    try:
        if not client:
            return f"{get_emotion('thinking')} AI service unavailable. Please try later!"

        completion = await client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.9,
            max_tokens=120,
            top_p=0.9
        )

        ai_reply = completion.choices[0].message.content
        ai_reply = f"{get_emotion(None, user_id)} {ai_reply}"

        if len(ai_reply) > 300:
            ai_reply = ai_reply[:297] + "..."

        chat_memory[chat_id].append({"role": "assistant", "content": ai_reply})
        return ai_reply

    except Exception:
        fallback_responses = [
            f"{get_emotion('crying')} Arre yaar, dimaag kaam nahi kar raha! Thoda ruk ke try karna?",
            f"{get_emotion('thinking')} Hmm... yeh to mushkil ho gaya. Phir se poocho?",
            f"{get_emotion('angry')} AI bhai mood off hai aaj! Baad me baat karte hain!",
            f"{get_emotion()} Oops! Connection issue. Kuch aur poocho?"
        ]
        return random.choice(fallback_responses)




# ================= CHAT =================
async def chat_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if update.effective_chat.type == "private" and not dm_enabled_users.get(user_id, True):
        return

    await update.message.reply_text("😼 Meow! Main sun raha hoon...")




# ================= WELCOME MEMBER =================
async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    new_status = update.chat_member.new_chat_member.status
    if new_status == ChatMemberStatus.MEMBER:
        member = update.chat_member.new_chat_member.user
        messages = [
            f"🎉 Welcome {member.first_name}! Khush aamdeed! 😊",
            f"🌟 Aao ji {member.first_name}! Group me welcome! 🫂",
            f"✨ Hey {member.first_name}! Great to have you here! 💖"
        ]
        await context.bot.send_message(update.effective_chat.id, random.choice(messages))

# ================= CHAT HANDLER WITH MENTION & PRIVATE =================
async def chat_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    user_id = message.from_user.id
    chat_id = message.chat.id
    bot = context.bot
    user_text = message.text

    # Check DM toggle
    if message.chat.type == Chat.PRIVATE and not dm_enabled_users.get(user_id, True):
        return

    # Bot mention / reply logic
    bot_username = (await bot.get_me()).username
    is_mention = f"@{bot_username}" in user_text if bot_username else False
    is_reply_to_bot = message.reply_to_message and message.reply_to_message.from_user.id == bot.id
    should_respond = message.chat.type == "private" or is_mention or is_reply_to_bot

    if should_respond:
        clean_text = user_text
        if bot_username and f"@{bot_username}" in clean_text:
            clean_text = clean_text.replace(f"@{bot_username}", "").strip()

        # Typing simulation
        await bot.send_chat_action(chat_id, "typing")
        await asyncio.sleep(random.uniform(0.5, 1.5))

        # AI reply
        response = await get_ai_response(chat_id, clean_text, user_id)
        await message.reply_text(response)
