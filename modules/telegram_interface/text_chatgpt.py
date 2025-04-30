from telegram import Update
from telegram.ext import ContextTypes
from services.openai_client import get_chatgpt_response

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    user_id = update.message.from_user.id
    chat_response = await get_chatgpt_response(user_id, user_message)
    await update.message.reply_text(chat_response)
