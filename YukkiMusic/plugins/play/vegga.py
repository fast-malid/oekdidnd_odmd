import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from YukkiMusic import app
from random import  choice, randint

#       #             #  #####  #####      ####
#        #           #  #         #            #     #
#          #        #  #####   #            #####     
#           #    #    #          #     ##    #     #
#              #       #####   ######   #     #
                
                
@app.on_message(
    command(["مطورين فيجا","المطورين","مطورين"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6154101472d61616307fe.jpg",
        caption=f"""**⩹━★⊷━𝐒𝐎𝐔𝐑𝐂𝐄 𝐕𝐄𝐆𝐀━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين فيجا ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━𝐒𝐎𝐔𝐑𝐂𝐄 𝐕𝐄𝐆𝐀━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⎖᳒𝐊𝐈𝐌𝐌𝐘⌯‹♱༄►", url=f"https://t.me/TOPVEGA"), 
                 ],[
                    InlineKeyboardButton(
                        "𓆩ᯓ𝐕𝐄↯𓆪", url=f"https://t.me/A7medNegm"),
                    InlineKeyboardButton(
                        "𝑨𝑳3𝑶𝑴𝑫𝑨", url=f"https://t.me/FM_3omda"),
                ],[
                
                    InlineKeyboardButton(
                        "★𝐒𝐎𝐔𝐑𝐂𝐄 𝐕𝐄𝐆𝐀⚡", url=f"https://t.me/SOURCEVEGA"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["احمد انجم","احمد","انجم","مبرمج","ve"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("A7medNegm")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━𝐒𝐎𝐔𝐑𝐂𝐄 𝐕𝐄𝐆𝐀━⊶★━⩺\n\n🧞‍♂️ ¦𝙺𝙸𝙽𝙶 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**⩹━★⊷━𝐒𝐎𝐔𝐑𝐂𝐄 𝐕𝐄𝐆𝐀━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
