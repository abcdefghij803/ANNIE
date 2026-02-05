from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums

import config
from NEXIOMUSIC import app


class BUTTONS(object):
    MtBUTTON = [
        [
            InlineKeyboardButton("Moon", url="https://t.me/btw_moon/557")
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
        ]
    ]

    ZBUTTON = [
        [
            InlineKeyboardButton("Kitty", url="https://t.me/+zOo21P9qDW4wZjk1"),
            InlineKeyboardButton("Annie", url="https://t.me/btw_moon"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
        ]
    ]

    ABUTTOhN = [
        [
            InlineKeyboardButton("ᴧʙσυᴛ", url="https://t.me/btw_moon/557"),
            InlineKeyboardButton("ʜєʟᴘ | ɪηғσ", callback_data="settings_back_helper"),
        ],
        [
            InlineKeyboardButton("ʙᴧsɪᴄ ɢυɪᴅє", callback_data="ABOUT_BACK HELP_GUIDE"),
            InlineKeyboardButton("ᴅσηᴧᴛє", callback_data="ABOUT_BACK HELP_DONATE"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
        ]
    ]

    PBUTTON = [
        [
            InlineKeyboardButton("˹ 🇲σ᭡፝֟ɳ🌙 ˼", url="https://t.me/btw_moon"),
            InlineKeyboardButton("˹ σᴡηєꝛ's ᴄʟᴧη 🎄 ˼", url="https://t.me/Grandxmasti"),
        ],
        [
            InlineKeyboardButton("˹ ʜєʟᴘ ˼", callback_data="MAIN_CP"),
            InlineKeyboardButton("˹ υᴘᴅᴧᴛєs ˼", url="https://t.me/kittyxupdates"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
        ]
    ]

    ABUTTON = [
        [
            InlineKeyboardButton("• ᴧηηɪє ᴠ2.0 •", callback_data="GUIDEBOT_CP"),
        ],
        [
            InlineKeyboardButton("˹ sυᴘᴘσʀᴛ ˼", url="https://t.me/grandxmasti"),
            InlineKeyboardButton("˹ σᴡηєꝛ ˼", callback_data="PROMOTION_CP"),
        ],
        [
            InlineKeyboardButton("˹ ʙᴧsɪᴄ ɢυɪᴅє  ˼", callback_data="MAIN_BACK HELP_ABOUT"),
            InlineKeyboardButton("˹ sσυꝛᴄє ˼", url="https://t.me/Kittyxupdates"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
        ]
    ]

    SBUTTON = [
        [
            InlineKeyboardButton("˹ ϻυsɪᴄ ˼", callback_data="settings_back_helper"),
            InlineKeyboardButton("˹ ϻᴧηᴧɢєϻєηᴛ ˼", callback_data="MANAGEMENT_CP"),
        ],
        [
            InlineKeyboardButton("˹ ᴧʟʟ ʙσᴛ's ˼", callback_data="TOOL_CP"),
            InlineKeyboardButton("˹ ɢᴧʟᴧxʏ ˼", callback_data="GALAXYBOT_CP"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
        ]
    ]

    GBUTTON = [
        [
            InlineKeyboardButton("˹ sυᴘᴘσʀᴛ ˼", url="https://t.me/Grandxmasti"),
            InlineKeyboardButton("˹ σᴡηєꝛ ˼", callback_data="PROMOTION_CP"),
        ],
        [
            InlineKeyboardButton("˹ ɢᴧʟᴧxʏ ˼", callback_data="GALAXYBOT_CP"),
            InlineKeyboardButton("˹ sσυꝛᴄє ˼", url="https://t.me/Kittyxupdates"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
        ]
    ]

    LBUTTON = [
        [
            InlineKeyboardButton("˹ sʜʏᴧꝛɪ ˼", url="https://t.me/Meowstric"),
            InlineKeyboardButton("˹ sυᴘᴘσʀᴛ ˼", url="https://t.me/grandxmasti"),
        ],
        [
            InlineKeyboardButton("˹ σᴡηєꝛ ˼", callback_data="PROMOTION_CP"),
            InlineKeyboardButton("˹ sσυꝛᴄє ˼", url="https://t.me/Kittyxupdates"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
        ]
    ]
