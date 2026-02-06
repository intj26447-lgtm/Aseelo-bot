import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

responses_asel = [
    "نعم؟ ناديتي الأسطورة؟ ",
    "وش تبي بسرعة لا تكثر كلام ",
    "أنا موجود… بس لا تصدعني",
]

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text.lower()

    if "هلا" in text:
        await update.message.reply_text("هلا بك… تو الناس ")

    elif "وينك" in text:
        await update.message.reply_text("كنت أراقبكم بصمت… لا تتحمس ")

    elif "اصيل" in text:
        await update.message.reply_text(random.choice(responses_asel))

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

print("AsEeL Bot is running...")
app.run_polling()
