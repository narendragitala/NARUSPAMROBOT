from telethon import events, Button
from config import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10
from AltronX.modules.help import *
import telethon

PythonButton = [
        [
        Button.inline("⛩️ ᴄσммαи∂ѕ ⛩️", data="help_back")
        ],
        [
        Button.url("🗼 ᴄнαт gʀρ 🗼", "https://t.me/II_4ST_FIGHTER_ll"),
        Button.url("🍹 ѕυρρσʀт 🍹", "https://t.me/SANATANI_IS_HERE")
        ],
        [
        Button.url("🍁 ＭＲ ＳＡＣＨＩＮ 🍁", "https://t.me/V_VIP_OWNER")
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
        TEXT = f"**🍹 нєℓℓσ му ∂єαʀ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\n⌾ 𝗜 𝗔𝗠 [{BotName}](tg://user?id={BotId})​**\n╭───────────────────╮\n\n"
        TEXT += f"» **🚩 ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ ‣ [ѕαиαтαиι](https://t.me/V_VIP_OWNER)**\n\n"
        TEXT += f"» **⛩️ 𝗦𝝙𝗡𝝙𝗧𝝙𝗡𝗜 || 𝗦𝗣𝝙𝗠​ ‣** `3.2`\n"
        TEXT += f"» **⛩️ 𝗦𝝙𝗡𝝙𝗧𝝙𝗡𝗜 || 𝗦𝗣𝝙𝗠​ ‣** `{telethon.__version__}`\n╰───────────────────╯"
        await event.client.send_file(
                event.chat_id,
                "https://telegra.ph/file/204854c3a0cb8cfeae36c.jpg",
                caption=TEXT, 
                buttons=PythonButton)
