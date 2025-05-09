from telegram import Update
from telegram.ext import ContextTypes
from core.intent_dispatcher import process_user_text  # Use process_user_text instead of get_chatgpt_response

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text.strip()
    user_id = update.message.from_user.id

    # Use process_user_text to handle the full pipeline
    chat_response = await process_user_text(user_id, user_message)

    # Send the response back to the user
    await update.message.reply_text(chat_response)