# handlers/help.py

from telegram import Update
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🛠 Available Commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "💬 Or just text me naturally like 'Turn on the lights!'"
    )