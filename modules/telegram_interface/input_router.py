from core.intent_dispatcher import process_user_text
from telegram.ext import ContextTypes

async def handle_text(update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle text messages from the user.
    """
    user_id = update.effective_user.id
    user_message = update.message.text.strip()

    # Process the user's message and get a response
    response = await process_user_text(user_id, user_message)

    # Send the response back to the user
    await update.message.reply_text(response)