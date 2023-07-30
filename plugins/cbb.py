#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>🤖 My Name: <a href='https://t.me/MT_FS_Bot'>MT File Store Bot</a>\n💥 Owner : <a href='https://t.me/i_like_surya'>Rohith</a>\n👨‍💻 Creator : <a href='https://t.me/Gowthaman2008'>Gowthaman</a>\n 📝 Language: <a href='https://www.python.org/'>Python3📚</a>\n 🎈 Library: <a href='https://docs.pyrogram.org/'>Pyrogram 💫</a>\n 🎉 Channel : @Movies_Tamizhaaas</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                   [      
                       InlineKeyboardButton("Contact Owner 💥", url="https://t.me/i_like_surya")
                       ],[
                       InlineKeyboardButton("Contact Creator ⚡", url="https://t.me/Gowthaman2008")
                    ],[
                        InlineKeyboardButton("🔒 Close", callback_data = "close")                   
                   ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
