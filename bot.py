import os
from flask import Flask
from threading import Thread
from telethon import TelegramClient, events, Button



client = Flask('')
@client.route('/')
def home():
    return "I am alive"

def run_http_server():
    client.run(host='0.0.0.0', port=8080) 

def keep_alive():
    t = Thread(target=run_http_server)
    os.system("cls")

    t.start()


# Bot credentials
# Enter api id and hash
API_ID = 0
API_HASH = ''

#Enter bot token
BOT_TOKEN = ' '

#Enter amdin id or id where u recive all text notification
admin_id = 0

bot = TelegramClient('shishya_bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    sender = await event.get_sender()
    name = sender.first_name or "Unknown"
    full_name = f"{sender.first_name or ''} {sender.last_name or ''}".strip()
    username = sender.username or "Not set"
    user_id = sender.id

    text = (
        f"✨ **Heyy `{name}`!** ✨\n\n"
        f"🆔 **User ID:** `{user_id}`\n"
        f"🔗 **Username:** @{username}\n\n"
        f"✉️ From this bot, you can contact [Shishya](https://t.me/ShishyaCode).\n\n\n"
        f"--->⛔️**Just drop your message and Shishya will reply soon** !"
    )

    # Inline keyboard
    buttons = [
        [Button.url("👨‍💻 Developer", "https://t.me/shishyapy"),
         Button.url("📢 Channel", "https://t.me/shishyacode")]
    ]

    await event.reply(text, buttons=buttons, link_preview=False)

    await bot.forward_messages(admin_id, event.message)
@bot.on(events.NewMessage)
async def forward_all_messages(event):
    if event.is_private and not event.raw_text.startswith('/start'):
        await bot.forward_messages(admin_id, event.message)

print("Bot is running...")
keep_alive()
bot.run_until_disconnected()
