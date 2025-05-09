from telegram import Update
from telegram.ext import ContextTypes
from core.conversation_manager import clear_conversation
async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update
    clear_conversation(user_id)
    await update.message.reply_text("Conversation reset. You can start fresh now!")