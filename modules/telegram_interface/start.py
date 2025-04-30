from telegram import Update
from telegram.ext import ContextTypes

async def start(update:Update, context:ContextTypes.DEFAULT_TYPE)->None:
    await update.message.reply_text(
        "👋 Hello! I am Luna. Welcome to your Smart Home AI Assistant.\n"
        "Feel free to text me anything you need!"
    )