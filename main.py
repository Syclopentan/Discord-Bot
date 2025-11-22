import discord
import os
from keep_alive import keep_alive

# إعدادات البوت (Intents) المطلوبة في النسخ الحديثة
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    # تغيير حالة البوت إلى "Playing A Game" أو أي شيء تريده
    await client.change_presence(activity=discord.Game(name="24/7 Online | Al-Fahad Group"))

# تشغيل سيرفر الويب لإبقاء البوت حياً
keep_alive()

# --- منطقة التوكين ---
# للتجربة المحلية (على جهازك) يمكنك ترك التوكين هنا.
# ولكن عند الرفع على GitHub/Render، يفضل استخدام os.getenv('TOKEN')
# التوكين الذي أرسلته:
my_secret = 'MTAyNDMyNTc3NDc1MDI2OTQ0MA.GAZ8Go.OmB5GWQV66XmPylqUePKV3c1pBn_VK-eAWj7TQ'

try:
  # يحاول جلب التوكين من متغيرات النظام (للأمان عند الرفع)
  token = os.getenv("TOKEN")
  if token is None:
      # إذا لم يجد متغير بيئة، يستخدم التوكين المكتوب مباشرة (للتجربة)
      token = my_secret
  
  client.run(token)
except Exception as e:
  print(f"Error: {e}")