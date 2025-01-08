from pyrogram import Client

import config

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="NEXIOASSISTANT1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="NEXIOASSISTANT2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="NEXIOASSISTANT3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="NEXIOASSISTANT4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="NEXIOASSISTANT5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"❖ ASSISTANT STARTING...")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("THE_INCRICIBLE")
                await self.one.join_chat("ZOYU_SUPPORT")
            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(config.LOGGER_ID, " ❖ ᴀssɪsᴛᴀɴᴛ ᴏɴᴇ sᴛᴀʀᴛᴇᴅ...🧡")
            except:
                LOGGER(__name__).error(
                    "❖ ASSISTANT ACCOUNTANT ONE HAS FAILED TO ACCESS THE LOG GROUP. MAKE SURE THAT YOU HAVE ADDED YOUR ASSISTANT TO YOUR LOG GROUP AND PROMOTED AS ADMIN !"
                )
                exit()
            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username
            assistantids.append(self.one.id)
            LOGGER(__name__).info(f"❖ ASSISTANT STARTED AS {self.one.name}")

        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("ALL_SANATANI_BOT")
                await self.two.join_chat("SANATANI_SUPPORT")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(config.LOGGER_ID, "❖ ᴀssɪsᴛᴀɴᴛ ᴛᴡᴏ sᴛᴀʀᴛᴇᴅ...❤️")
            except:
                LOGGER(__name__).error(
                    "❖ ASSISTANT ACCOUNTANT TWO HAS FAILED TO ACCESS THE LOG GROUP. MAKE SURE THAT YOU HAVE ADDED YOUR ASSISTANT TO YOUR LOG GROUP AND PROMOTED AS ADMIN !"
                )
                exit()
            self.two.id = self.two.me.id
            self.two.name = self.two.me.mention
            self.two.username = self.two.me.username
            assistantids.append(self.two.id)
            LOGGER(__name__).info(f"❖ ASSISTANT TWO STARTED AS {self.two.name}")

        if config.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("ALL_SANATANI_BOT")
                await self.three.join_chat("SANATANI_SUPPORT")
            except:
                pass
            assistants.append(3)
            try:
                await self.three.send_message(config.LOGGER_ID, "❖ ᴀssɪsᴛᴀɴᴛ ᴛʜʀᴇᴇ sᴛᴀʀᴛᴇᴅ...💙")
            except:
                LOGGER(__name__).error(
                    "❖ ASSISTANT ACCOUNTANT THREE HAS FAILED TO ACCESS THE LOG GROUP. MAKE SURE THAT YOU HAVE ADDED YOUR ASSISTANT TO YOUR LOG GROUP AND PROMOTED AS ADMIN !"
                )
                exit()
            self.three.id = self.three.me.id
            self.three.name = self.three.me.mention
            self.three.username = self.three.me.username
            assistantids.append(self.three.id)
            LOGGER(__name__).info(f"❖ ASSISTANT THREE STARTED AS {self.three.name}")

        if config.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("ALL_SANATANI_BOT")
                await self.four.join_chat("SANATANI_SUPPORT")
            except:
                pass
            assistants.append(4)
            try:
                await self.four.send_message(config.LOGGER_ID, "❖ ᴀssɪsᴛᴀɴᴛ ғᴏᴜʀ sᴛᴀʀᴛᴇᴅ...💛")
            except:
                LOGGER(__name__).error(
                    "❖ ASSISTANT ACCOUNTANT FOUR HAS FAILED TO ACCESS THE LOG GROUP. MAKE SURE THAT YOU HAVE ADDED YOUR ASSISTANT TO YOUR LOG GROUP AND PROMOTED AS ADMIN !"
                )
                exit()
            self.four.id = self.four.me.id
            self.four.name = self.four.me.mention
            self.four.username = self.four.me.username
            assistantids.append(self.four.id)
            LOGGER(__name__).info(f"❖ ASSISTANT FOUR STARTED AS {self.four.name}")

        if config.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("ALL_SANATANI_BOT")
                await self.five.join_chat("SANATANI_SUPPORT")
            except:
                pass
            assistants.append(5)
            try:
                await self.five.send_message(config.LOGGER_ID, "❖ ᴀssɪsᴛᴀɴᴛ ғɪᴠᴇ sᴛᴀʀᴛᴇᴅ...🤍")
            except:
                LOGGER(__name__).error(
                    "❖ ASSISTANT ACCOUNTANT FIVE HAS FAILED TO ACCESS THE LOG GROUP. MAKE SURE THAT YOU HAVE ADDED YOUR ASSISTANT TO YOUR LOG GROUP AND PROMOTED AS ADMIN !"
                )
                exit()
            self.five.id = self.five.me.id
            self.five.name = self.five.me.mention
            self.five.username = self.five.me.username
            assistantids.append(self.five.id)
            LOGGER(__name__).info(f"❖ ASSISTANT FIVE STARTED AS {self.five.name}")

    async def stop(self):
        LOGGER(__name__).info(f"❖ STOPPING ASSISTANTS...")
        try:
            if config.STRING1:
                await self.one.stop()
            if config.STRING2:
                await self.two.stop()
            if config.STRING3:
                await self.three.stop()
            if config.STRING4:
                await self.four.stop()
            if config.STRING5:
                await self.five.stop()
        except:
            pass
