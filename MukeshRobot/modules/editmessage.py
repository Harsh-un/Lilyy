from pyrogram import Client, filters
import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters
from pyrogram.types import Message
import time
import psutil
import platform
import logging
from config import OWNER_ID, BOT_USERNAME
from config import *
from Lilyy import MukeshRobot as app
import pyrogram
from pyrogram.errors import FloodWait




@app.on_edited_message(filters.group & ~filters.me)
async def delete_edited_messages(client, edited_message):
    await edited_message.delete()
    user_mention = from_user.mention
    await edited_message.reply_text(f"{user_mention} ᴇᴅɪᴛᴇᴅ ᴀ ᴍᴇssᴀɢᴇ ᴀɴᴅ I ᴅᴇʟᴇᴛᴇᴅ ɪᴛ🤡👽")

