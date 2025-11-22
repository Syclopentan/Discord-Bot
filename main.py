import discord
import os
from keep_alive import keep_alive

# إعدادات البوت (Intents)
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    # هنا يمكنك تغيير حالة البوت
    await client.change_presence(activity=discord.Game(name="24/7 Online | Al-Fahad Group"))

# تشغيل سيرفر الويب للبقاء متصلاً
keep_alive()

# تشغيل البوت باستخدام التوكين المخفي في السيرفر
try:
    token = os.getenv("TOKEN")
    if not token:
        print("⚠️ Error: Token not found! Please add 'TOKEN' in Render Environment Variables.")
    else:
        client.run(token)
except Exception as e:
    print(f"Error: {e}")