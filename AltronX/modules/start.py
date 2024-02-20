from telethon import events, Button
from config import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10
from AltronX.modules.help import *
import telethon

PythonButton = [
        [
        Button.inline("⛩️ ᴄσммαи∂ѕ ⛩️", data="help_back")
        ],
        [
        Button.url("🗼 ᴄнαт gʀρ 🗼", "https://t.me/Professor_Ki_Duniya"),
        Button.url("🍹 ѕυρρσʀт 🍹", "https://t.me/Professor_Ki_Duniya")
        ],
        [
        Button.url("🍁 ＰＲＯＦＥＳＳＯＲ 🍁", "https://t.me/SOURABH_OWNER")
        ]
        ]


@MK1.on(events.NewMessage(pattern="/start"))
@MK2.on(events.NewMessage(pattern="/start"))
@MK3.on(events.NewMessage(pattern="/start"))
@MK4.on(events.NewMessage(pattern="/start"))
@MK5.on(events.NewMessage(pattern="/start"))
@MK6.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK8.on(events.NewMessage(pattern="/start"))
@MK9.on(events.NewMessage(pattern="/start"))
@MK10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        BotName = AltBot.first_name
        BotId = AltBot.id
        TEXT = f"**🍹 ʜᴇʟʟᴇ ᴍʏ ᴅᴇᴀʀ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\n
        TEXT += f"⌾ 𝗜 𝗔𝗠 [{BotName}](tg://user?id={BotId})​**\n╭───────────────────╮\n\n"
        TEXT += f"➜ ** ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ ‣ [ᴘʀᴏғᴇssᴏʀ](https://t.me/SOURABH_OWNER)**\n\n"
        TEXT += f"➲ ** 𝗣𝗥𝗢𝗙𝗘𝗦𝗦𝗢𝗥 || 𝗦𝗣𝝙𝗠​ ‣** `3.2`\n"
        TEXT += f"➲ ** 𝗣𝗥𝗢𝗙𝗘𝗦𝗦𝗢𝗥 || 𝗦𝗣𝝙𝗠​ ‣** `{telethon.__version__}`\n\n╰───────────────────╯"
        await event.client.send_file(
                event.chat_id,
                "https://telegra.ph/file/e6cb4ad88300b6c4ed855.jpg",
                caption=TEXT, 
                buttons=PythonButton)
