from config import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10, SUDO_USERS, CMD_HNDLR as hl
from telethon import events, Button


PythonHelp = f" иαяυᴊααт ѕραм нєℓρ мєиυ \n\n» **ᴄℓιᴄк σи вєℓσω вυттσиѕ fσʀ нєℓρ**\n» **∂єνєℓσρєʀ :-: @MR_NARU**"


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
       await event.client.send_file(event.chat_id,
                                  "https://telegra.ph/file/f16ec12ab36582b3902fb.jpg",
                                  caption=PythonHelp,
                                  buttons=[
           [
            Button.inline("⦿ ＳＰＡＭ ⦿", data="spam"),
            Button.inline("⦿ ＲＡＩＤ ⦿", data="raid"),
           ],
           [
            Button.inline("⦿ ＥＸＴＲＡ ⦿", data="extra"),
           ],
           [    
            Button.url("⦿ ＣＨＡＮＮＥＬ ⦿", "https://t.me/BROKENSHAYRI1"),
            Button.url("⦿ ＳＵＰＰＯＲＴ ⦿", "https://t.me/SHAYRIGALIBKI")
           ],
           ],
           )


extra_msg = f"""
**:- єxтяα ᴄσммαи∂ :**

ＵＳＥＲＢＯＴ: ＵＳＥＲＢＯＴ ＣＭＮＤ
  1) {hl}ping 
  2) {hl}reboot
  3) {hl}sudo <reply to user>  --> Owner Cmd
  4) {hl}logs --> Owner Cmd

єᴄнσ :- тσ αᴄтινє єᴄнσ σи αиу υѕєя
  1) {hl}echo <reply to user>
  2) {hl}rmecho <reply to user>

ℓєανє :- тσ ℓєανє gʀσυρ / ᴄнαииєℓ
  1) {hl}leave <group/chat id>
  2) {hl}leave : Type in the Group bot will auto leave that group


**© @NARU_JAAT**
"""

                 
raid_msg = f"""
**ᴄнυ∂αι ᴄσммαи∂ ( ʀαι∂ ):**

𝗥𝗔𝗜𝗗 :-: αᴄтιναтєѕ ʀαι∂ σи αиу ιи∂ινι∂υαℓ υѕєʀ fσʀ ∂ιgєи  ʀαиgє.
  1) {hl}raid <count> <username>
  2) {hl}raid <count> <reply to user>

𝗥𝗘𝗣𝗟𝗬 𝗥𝗔𝗜𝗗 : αᴄтιναтєѕ ʀαρℓу ʀαι∂ σи тнє υѕєʀ !!
  1) {hl}rraid <replying to user>
  2) {hl}rraid <username>

𝗗-𝗥𝗘𝗣𝗟𝗬 𝗥𝗔𝗜𝗗 : ∂єαᴄтιναтєѕ ʀєρℓу ʀαι∂ σи тнє υѕєʀ !!
  1) {hl}drraid <replying to user>
  2) {hl}drraid <username>

𝗠-𝗥𝗔𝗜𝗗 : ℓσνє ʀαι∂ σи тнє υѕєʀ !!
  1) {hl}mraid <count> <username>
  2) {hl}mraid <count> <reply to user>

𝗦-𝗥𝗔𝗜𝗗: ѕнαуαʀι ʀαι∂ σи тнє υѕєʀ !!
  1) {hl}sraid <count> <username>
  2) {hl}sraid <count> <reply to user>

𝗖-𝗥𝗔𝗜𝗗 : αвᴄ∂ ʀαι∂ σи тнє υѕєʀ !!
  1) {hl}craid <count> <username>
  2) {hl}craid <count> <reply to user>


**© @MR_NARU**
"""

spam_msg = f"""
**» ѕραм ᴄσммαи∂:**

𝗦𝗣𝗔𝗠 ; ѕραмѕ α мєѕѕαgє.
  1) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
  2) {hl}spam <count> <replying any message>

𝗣𝗢𝗥𝗡 𝗦𝗣𝗔𝗠 : ρσʀиσgʀαρну ѕραм.
  1) {hl}pspam <count>

𝗛𝗔𝗡𝗚 : ѕραмѕ нαиgιиg мєѕѕєg fσʀ gινєи ᴄσυитєʀ.
  1) {hl}hang <counter> (you can reply any message if you want bot to reply that message and do spamming)


** © @MR_NARU**
"""                     
           
           
@MK1.on(events.CallbackQuery(pattern=r"help_back"))
@MK2.on(events.CallbackQuery(pattern=r"help_back"))
@MK3.on(events.CallbackQuery(pattern=r"help_back"))
@MK4.on(events.CallbackQuery(pattern=r"help_back"))
@MK5.on(events.CallbackQuery(pattern=r"help_back"))
@MK6.on(events.CallbackQuery(pattern=r"help_back"))
@MK7.on(events.CallbackQuery(pattern=r"help_back"))
@MK8.on(events.CallbackQuery(pattern=r"help_back"))
@MK9.on(events.CallbackQuery(pattern=r"help_back"))
@MK10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
   if event.query.user_id in SUDO_USERS:    
      await event.edit(
            PythonHelp,
            buttons=[
           [
            Button.inline("⦿ ＳＰＡＭ ⦿", data="spam"),
            Button.inline("⦿ ＲＡＩＤ ⦿", data="raid"),
           ],
           [
            Button.inline("⦿ ＥＸＴＲＡ ⦿", data="extra"),
           ],
           [
            Button.url("⦿ ＣＨＡＮＮＥＬ ⦿", "https://t.me/BROKENSHAYRI1"),
            Button.url("⦿ ＳＵＰＰＯＲＴ ⦿", "https://t.me/SHAYRIGALIBKI")
           ],
           ],
        )           
   else:
        await event.answer("𝗡𝗔𝗥𝗨𝗝𝗔𝗔𝗧 [ @MR_NARU ] 𝗗𝗠 𝗞𝗔𝗥 𝗦𝗨𝗗𝗢 𝗠𝗜𝗟 𝗝𝗔𝗬𝗘𝗚𝗔︎ || 𝗘𝗞 𝗕𝗔𝗔𝗥 𝗣𝗔𝗣𝗔 𝗕𝗢𝗟 𝗡𝗔 𝗥𝗔𝗡𝗗𝗜 𝗞𝗘", cache_time=0, alert=True)


@MK1.on(events.CallbackQuery(pattern=r"spam"))
@MK2.on(events.CallbackQuery(pattern=r"spam"))
@MK3.on(events.CallbackQuery(pattern=r"spam"))
@MK4.on(events.CallbackQuery(pattern=r"spam"))
@MK5.on(events.CallbackQuery(pattern=r"spam"))
@MK6.on(events.CallbackQuery(pattern=r"spam"))
@MK7.on(events.CallbackQuery(pattern=r"spam"))
@MK8.on(events.CallbackQuery(pattern=r"spam"))
@MK9.on(events.CallbackQuery(pattern=r"spam"))
@MK10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
   if event.query.user_id in SUDO_USERS:    
       await event.edit(spam_msg,
            buttons=[[Button.inline("< ＢＡＣＫ", data="help_back"),],],
            ) 
   else:
        await event.answer("𝗡𝗔𝗥𝗨𝗝𝗔𝗔𝗧 [ @MR_NARU ] 𝗗𝗠 𝗞𝗔𝗥 𝗦𝗨𝗗𝗢 𝗠𝗜𝗟 𝗝𝗔𝗬𝗘𝗚𝗔︎ || 𝗘𝗞 𝗕𝗔𝗔𝗥 𝗣𝗔𝗣𝗔 𝗕𝗢𝗟 𝗡𝗔 𝗥𝗔𝗡𝗗𝗜 𝗞𝗘", cache_time=0, alert=True)


@MK1.on(events.CallbackQuery(pattern=r"raid"))
@MK2.on(events.CallbackQuery(pattern=r"raid"))
@MK3.on(events.CallbackQuery(pattern=r"raid"))
@MK4.on(events.CallbackQuery(pattern=r"raid"))
@MK5.on(events.CallbackQuery(pattern=r"raid"))
@MK6.on(events.CallbackQuery(pattern=r"raid"))
@MK7.on(events.CallbackQuery(pattern=r"raid"))
@MK8.on(events.CallbackQuery(pattern=r"raid"))
@MK9.on(events.CallbackQuery(pattern=r"raid"))
@MK10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
     if event.query.user_id in SUDO_USERS:
        await event.edit(raid_msg,
            buttons=[[Button.inline("< ＢＡＣＫ", data="help_back"),],],
            )  
     else:
        await event.answer("𝗡𝗔𝗥𝗨𝗝𝗔𝗔𝗧 [ @MR_NARU ] 𝗗𝗠 𝗞𝗔𝗥 𝗦𝗨𝗗𝗢 𝗠𝗜𝗟 𝗝𝗔𝗬𝗘𝗚𝗔︎ || 𝗘𝗞 𝗕𝗔𝗔𝗥 𝗣𝗔𝗣𝗔 𝗕𝗢𝗟 𝗡𝗔 𝗥𝗔𝗡𝗗𝗜 𝗞𝗘", cache_time=0, alert=True)


@MK1.on(events.CallbackQuery(pattern=r"extra"))
@MK2.on(events.CallbackQuery(pattern=r"extra"))
@MK3.on(events.CallbackQuery(pattern=r"extra"))
@MK4.on(events.CallbackQuery(pattern=r"extra"))
@MK5.on(events.CallbackQuery(pattern=r"extra"))
@MK6.on(events.CallbackQuery(pattern=r"extra"))
@MK7.on(events.CallbackQuery(pattern=r"extra"))
@MK8.on(events.CallbackQuery(pattern=r"extra"))
@MK9.on(events.CallbackQuery(pattern=r"extra"))
@MK10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
   if event.query.user_id in SUDO_USERS:
        await event.edit(extra_msg,
            buttons=[[Button.inline("< ＢＡＣＫ", data="help_back"),],],
            )
   else:
        await event.answer("𝗡𝗔𝗥𝗨𝗝𝗔𝗔𝗧 [ @MR_NARU ] 𝗗𝗠 𝗞𝗔𝗥 𝗦𝗨𝗗𝗢 𝗠𝗜𝗟 𝗝𝗔𝗬𝗘𝗚𝗔︎ || 𝗘𝗞 𝗕𝗔𝗔𝗥 𝗣𝗔𝗣𝗔 𝗕𝗢𝗟 𝗡𝗔 𝗥𝗔𝗡𝗗𝗜 𝗞𝗘", cache_time=0, alert=True)
