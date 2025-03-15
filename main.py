import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess
import urllib.parse
import yt_dlp
import cloudscraper
from logs import logging
from bs4 import BeautifulSoup
import core as helper
from utils import progress_bar
from vars import API_ID, API_HASH, BOT_TOKEN
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput
from pytube import YouTube
from aiohttp import web

from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

credit ="𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎" 
# Initialize the bot
bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Define aiohttp routes
routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("https://text-leech-bot-for-render.onrender.com/")

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

async def start_bot():
    await bot.start()
    print("Bot is up and running")

async def stop_bot():
    await bot.stop()

async def main():
    if WEBHOOK:
        # Start the web server
        app_runner = web.AppRunner(await web_server())
        await app_runner.setup()
        site = web.TCPSite(app_runner, "0.0.0.0", PORT)
        await site.start()
        print(f"Web server started on port {PORT}")

    # Start the bot
    await start_bot()

    # Keep the program running
    try:
        while True:
            await bot.polling()  # Run forever, or until interrupted
    except (KeyboardInterrupt, SystemExit):
        await stop_bot()
    

async def start_bot():
    await bot.start()
    print("Bot is up and running")

async def stop_bot():
    await bot.stop()

async def main():
    if WEBHOOK:
        # Start the web server
        app_runner = web.AppRunner(await web_server())
        await app_runner.setup()
        site = web.TCPSite(app_runner, "0.0.0.0", PORT)
        await site.start()
        print(f"Web server started on port {PORT}")

    # Start the bot
    await start_bot()

    # Keep the program running
    try:
        while True:
            await asyncio.sleep(3600)  # Run forever, or until interrupted
    except (KeyboardInterrupt, SystemExit):
        await stop_bot()
        
import random

# Inline keyboard for start command
keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="📞 Contact", url="https://t.me/Nikhil_saini_khe"),
            InlineKeyboardButton(text="🛠️ Help", url="https://t.me/+3k-1zcJxINYwNGZl"),
        ],
    ]
)

# Inline keyboard for busy status
Busy = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="📞 Contact", url="https://t.me/Nikhil_saini_khe"),
            InlineKeyboardButton(text="🛠️ Help", url="https://t.me/+3k-1zcJxINYwNGZl"),
        ],
    ]
)

# Image URLs for the random image feature
image_urls = [
    "https://tinypic.host/images/2025/02/07/IMG_20250207_224444_975.jpg",
    "https://tinypic.host/images/2025/02/07/DeWatermark.ai_1738952933236-1.png",
    # Add more image URLs as needed
]

cookies_file_path= "youtube_cookies.txt"

@bot.on_message(filters.command("cookies") & filters.private)
async def cookies_handler(client: Client, m: Message):
    await m.reply_text(
        "Please upload the cookies file (.txt format).",
        quote=True
    )

    try:
        # Wait for the user to send the cookies file
        input_message: Message = await client.listen(m.chat.id)

        # Validate the uploaded file
        if not input_message.document or not input_message.document.file_name.endswith(".txt"):
            await m.reply_text("Invalid file type. Please upload a .txt file.")
            return

        # Download the cookies file
        downloaded_path = await input_message.download()

        # Read the content of the uploaded file
        with open(downloaded_path, "r") as uploaded_file:
            cookies_content = uploaded_file.read()

        # Replace the content of the target cookies file
        with open(cookies_file_path, "w") as target_file:
            target_file.write(cookies_content)

        await input_message.reply_text(
            "✅ Cookies updated successfully.\n📂 Saved in `youtube_cookies.txt`."
        )

    except Exception as e:
        await m.reply_text(f"⚠️ An error occurred: {str(e)}")
        
# Start command handler
@bot.on_message(filters.command(["start"]))
async def start_command(bot: Client, message: Message):
    # Send a loading message
    loading_message = await bot.send_message(
        chat_id=message.chat.id,
        text="Loading... ⏳🔄"
    )
  
    # Choose a random image URL
    random_image_url = random.choice(image_urls)
    
    # Caption for the image
    caption = (
        "🌟 Welcome Boss😸! 🌟\n\n"
        "➽ I am powerful uploader bot 📥\n\n➽ Send Direct link /.txt file To Extract\n\n➽ 𝐔𝐬𝐞 /Stop for **Stop** ⛔ working process \n\n➽ 𝐔𝐬𝐞 /cookies for update YouTube cookies.\n\n➽ 𝐔𝐬𝐞 /logs to see your bot logs.\n\n➽ 𝐌𝐚𝐝𝐞 𝐁𝐲: 𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎 🦁"
    )

    await asyncio.sleep(1)
    await loading_message.edit_text(
        "Initializing Uploader bot... 🤖\n\n"
        "Progress: ⬜⬜⬜⬜⬜⬜⬜⬜⬜ 0%\n\n"
    )

    await asyncio.sleep(1)
    await loading_message.edit_text(
        "Loading features... ⏳\n\n"
        "Progress: 🟥🟥⬜⬜⬜⬜⬜⬜ 25%\n\n"
    )
    
    await asyncio.sleep(1)
    await loading_message.edit_text(
        "This may take a moment, sit back and relax! 😊\n\n"
        "Progress: 🟧🟧🟧🟧⬜⬜⬜⬜ 50%\n\n"
    )

    await asyncio.sleep(1)
    await loading_message.edit_text(
        "Checking Bot Status... 🔍\n\n"
        "Progress: 🟨🟨🟨🟨🟨🟨⬜⬜ 75%\n\n"
    )

    await asyncio.sleep(1)
    await loading_message.edit_text(
        "Checking status Ok... \n**ᴊᴏɪɴ ᴏᴜʀ <a href='https://t.me/+1e-r94cF6yE3NzA1'>ᴛᴇʟᴇɢʀᴀᴍ Group</a>**\n\n"
        "Progress:🟩🟩🟩🟩🟩🟩🟩🟩🟩 100%\n\n"
    )
        
    # Send the image with caption and buttons
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=random_image_url,
        caption=caption,
        reply_markup=keyboard
    )

    # Delete the loading message
    await loading_message.delete()
    

@bot.on_message(filters.command(["logs"]) )
async def send_logs(bot: Client, m: Message):
    try:
        with open("logs.txt", "rb") as file:
            sent= await m.reply_text("**📤 Sending you ....**")
            await m.reply_document(document=file)
            await sent.delete(True)
    except Exception as e:
        await m.reply_text(f"Error sending logs: {e}")

@bot.on_message(filters.command(["stop"]) )
async def restart_handler(_, m):
    await m.reply_text("🦅ˢᵗᵒᵖᵖᵉᵈ ᵇᵃᵇʸ💞", True)
    os.execl(sys.executable, sys.executable, *sys.argv)

@bot.on_message(filters.document & filters.private | filters.text & filters.private)
async def document_or_text_handler(bot: Client, m: Message):
    
    if m.document:
        if not m.document.file_name.endswith(".txt"):
            await m.reply_text("Please upload a valid .txt file.")
            return

        editable = await m.reply_text(f"**🔹Processing your TXT file...\n🔁Please wait...⏳**")
        x = await m.download()
        await m.delete()
        file_name, ext = os.path.splitext(os.path.basename(x))
        try:    
            with open(x, "r") as f:
                content = f.read()
            content = content.split("\n")
            links = []
            for i in content:
                links.append(i.split("://", 1))
            os.remove(x)
        except:
            await m.reply_text("Invalid file input.")
            os.remove(x)
            return
    elif m.text:
        editable = await m.reply_text(f"**🔹Processing your text message...\n🔁Please wait...⏳**")
        content = m.text.split("\n")
        links = []
        for i in content:
            links.append(i.strip())
    
    await editable.edit(f"Total 🔗 links found are __**{len(links)}**__\n\nSend From where you want to download initial is **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)
    try:
        arg = int(raw_text)
    except:
        arg = 1
    await editable.edit("**Enter Your Batch Name**\n\n**Send __1__ for use default.**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    if raw_text0 == '1':
        b_name = file_name if m.document else "Default_Batch"
    else:
        b_name = raw_text0

    await editable.edit("**╭━━━━❰ᴇɴᴛᴇʀ ʀᴇꜱᴏʟᴜᴛɪᴏɴ❱━➣\n┣━━⪼ send 144  for 144p\n┣━━⪼ send 240  for 240p\n┣━━⪼ send 360  for 360p\n┣━━⪼ send 480  for 480p\n┣━━⪼ send 720  for 720p\n┣━━⪼ send 1080 for 1080p\n╰━━━━━━━━━━━━━➣**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
        res = "UN"

    await editable.edit("**Enter Your Name**\n\n**Send __1__ for use default**")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    # Default credit message
    credit = "️𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎 🕊️⁪⁬⁮⁮⁮"
    if raw_text3 == '1':
        CR = '𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎 🕊️'
    elif raw_text3:
        CR = raw_text3
    else:
        CR = credit

    pw_token = f"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDEyNjcwMDYuMTgzLCJkYXRhIjp7Il9pZCI6IjY1YzFlZTE1ODZmMTQ4MDAxMjdkOWIxOSIsInVzZXJuYW1lIjoiNjM5NDM4MzAzMCIsImZpcnN0TmFtZSI6IkRlZXBhbnNoIiwibGFzdE5hbWUiOiJNaXNocmEiLCJvcmdhbml6YXRpb24iOnsiX2lkIjoiNWViMzkzZWU5NWZhYjc0NjhhNzlkMTg5Iiwid2Vic2l0ZSI6InBoeXNpY3N3YWxsYWguY29tIiwibmFtZSI6IlBoeXNpY3N3YWxsYWgifSwiZW1haWwiOiJyYWplc2htaXNocmExOTc5MEBnbWFpbC5jb20iLCJyb2xlcyI6WyI1YjI3YmQ5NjU4NDJmOTUwYTc3OGM2ZWYiLCI1Y2M5NWEyZThiZGU0ZDY2ZGU0MDBiMzciXSwiY291bnRyeUdyb3VwIjoiSU4iLCJ0eXBlIjoiVVNFUiJ9LCJpYXQiOjE3NDA2NjIyMDZ9.hDoYcFo9uxxhajHudIZtqgtqd3G8QdNxQSS9qkdjNJg"
    
        
    await editable.edit("**Enter Your PW Token For 𝐌𝐏𝐃 𝐔𝐑𝐋**\n\n**Send  __0__  for use default**")
    input4: Message = await bot.listen(editable.chat.id)
    raw_text4 = input4.text
    await input4.delete(True)
    if raw_text4 == '0':
        PW = pw_token
    else:
        PW = raw_text4
        
    await editable.edit("⚪Send   ☞ **no** for **video** format\n\n🔘Send   ☞ **No** for **Document** format")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    await m.reply_text(
        f"__**🎯Target Batch :  {b_name} **__"
    )

    count = int(raw_text)    
    try:
        for i in range(arg-1, len(links)):
            Vxy = links[i].replace("file/d/", "uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing", "")
            url = "https://" + Vxy
            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            if "acecwply" in url:
                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={raw_text2}]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "{url}"'

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif 'videos.classplusapp' in url or "tencdn.classplusapp" in url or "webvideos.classplusapp.com" in url or "media-cdn-alisg.classplusapp.com" in url or "videos.classplusapp" in url or "vi" in url:
                url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJjb3Vyc2VJZCI6IjQ1NjY4NyIsInR1dG9ySWQiOm51bGwsIm9yZ0lkIjo0ODA2MTksImNhbXB1c1VybCI6Imh0dHBzOi8vY2xhc3NwbHVzYXBwLmNvbS9jb250ZW50L29yZ2FuaXphdGlvbnMvZGVmYXVsdC9jb3Vyc2VzLzQ4MDYxOS9jbGFzc2VzL2NvdXJzZXMvNDU2Njg3In0sImlzcyI6IkV4YW1QbHVzIiwiYXVkIjoiQ2xhc3NQbHVzIiwiZXhwIjoxNzU2OTk1MzI2fQ.jE1yieE8x8vVbHlAVEE9Q3pPZ8JQ7wKXl7-L3xjE_HU'}).json()['signedUrl']

            elif '/master.mpd' in url:
                vid_id = url.split("/")[-2]
                url = f"https://pwplayer-0e2dbbdc0989.herokuapp.com/player?url=https://d1d34p8vz63oiq.cloudfront.net/{vid_id}/master.m3u8?token={PW}"

            name1 = links[i].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "")
            name = f'{name1[:60]}'

            if 'cpvod.testbook.com' in url:
                url = requests.get(f'https://mon-key-3612a8154345.herokuapp.com/get_keys?url={url}', headers={'x-access-token': 'eyJjb3Vyc2VJZCI6IjQ1NjY4NyIsInR1dG9ySWQiOm51bGwsIm9yZ0lkIjo0ODA2MTksImNhbXB1c1VybCI6Imh0dHBzOi8vY2xhc3NwbHVzYXBwLmNvbS9jb250ZW50L29yZ2FuaXphdGlvbnMvZGVmYXVsdC9jb3Vyc2VzLzQ4MDYxOS9jbGFzc2VzL2NvdXJzZXMvNDU2Njg3In0sImlzcyI6IkV4YW1QbHVzIiwiYXVkIjoiQ2xhc3NQbHVzIiwiZXhwIjoxNzU2OTk1MzI2fQ.jE1yieE8x8vVbHlAVEE9Q3pPZ8JQ7wKXl7-L3xjE_HU'}).json()['signedUrl']

            if "/master.mpd" in url:
                if "https://sec1.pw.live/" in url:
                    url = url.replace("https://sec1.pw.live/", "https://d1d34p8vz63oiq.cloudfront.net/")
                    print(url)
                else:
                    url = url

                print("mpd check")
                key = await helper.get_drm_keys(url)
                print(key)
                await m.reply_text(f"got keys form api : \n`{key}`")

            if "/master.mpd" in url:
                cmd = f" yt-dlp -k --allow-unplayable-formats -f bestvideo.{quality} --fixup never {url} "
                print("counted")

            if "edge.api.brightcove.com" in url:
                bcov = 'bcov_auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MjQyMzg3OTEsImNvbiI6eyJpc0FkbWluIjpmYWxzZSwiYXVzZXIiOiJVMFZ6TkdGU2NuQlZjR3h5TkZwV09FYzBURGxOZHowOSIsImlkIjoiZEUxbmNuZ'
                url = url.split("bcov_auth")[0] + bcov

            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'

            elif "youtube.com" in url or "youtu.be" in url:
                cmd = f'yt-dlp --cookies youtube_cookies.txt -f "{ytf}" "{url}" -o "{name}.mp4"'

            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:
                cc = f'**——— ✦  {str(count).zfill(3)} ✦ ———**\n\n**🎞️ Title : ** {name1} **[{res}]**.mp4\n\n**📚 Course :** {b_name}\n\n**🌟 Extracted By : {CR}\n**'
                cc1 = f'**——— ✦  {str(count).zfill(3)} ✦ ———**\n\n**📁 Title : ** {name1} .pdf\n\n**📚 Course :** {b_name}\n\n**🌟 Extracted By : {CR}\n**'
                cczip = f'**——— ✦  {str(count).zfill(3)} ✦ ———**\n\n**📁 Title : ** {name1} .zip\n\n**📚 Course :** {b_name}\n\n**🌟 Extracted By : {CR}\n**'
                ccimg = f'**——— ✦  {str(count).zfill(3)} ✦ ———**\n\n**📁 Title : ** {name1} .jpg\n\n**📚 Course :** {b_name}\n\n**🌟 Extracted By : {CR}\n**'

                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id, document=ka, caption=cc1)
                        count += 1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        count += 1
                        continue

                elif ".pdf" in url:
                    try:
                        await asyncio.sleep(4)
                        url = url.replace(" ", "%20")
                        scraper = cloudscraper.create_scraper()
                        response = scraper.get(url)
                        if response.status_code == 200:
                            with open(f'{name}.pdf', 'wb') as file:
                                file.write(response.content)
                            await asyncio.sleep(4)
                            copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                            count += 1
                            os.remove(f'{name}.pdf')
                        else:
                            await m.reply_text(f"Failed to download PDF: {response.status_code} {response.reason}")
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        count += 1
                        continue

                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                        count += 1
                        os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        count += 1
                        continue

                elif ".zip" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.zip" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.zip', caption=cczip)
                        count += 1
                        os.remove(f'{name}.zip')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        count += 1
                        continue

                elif ".jpg" in url or ".png" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.jpg" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_photo(chat_id=m.chat.id, document=f'{name}.jpg', caption=ccimg)
                        count += 1
                        os.remove(f'{name}.jpg')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        count += 1
                        continue

                else:
                    Show = f"**⚡Dᴏᴡɴʟᴏᴀᴅ Sᴛᴀʀᴛᴇᴅ...⏳**\n\n🔗𝐈𝐧𝐝𝐞𝐱 » {str(count)}/{len(links)}\n\n**📚𝐓𝐢𝐭𝐥𝐞** » `{name}\n\n🍁𝐐𝐮𝐚𝐥𝐢𝐭𝐲 » {raw_text2}p`\n\n**✦𝐁𝐨𝐭 𝐌𝐚𝐝𝐞 𝐁𝐲 ✦ 𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎🐦"
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"⚠️ 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐈𝐧𝐭𝐞𝐫𝐮𝐩𝐭𝐞𝐝\n\n⚠️ 𝐍𝐚𝐦𝐞 » {name}\n"
                )
                count += 1
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("🕊️Done Baby💞")



bot.run()
if __name__ == "__main__":
    asyncio.run(main())
