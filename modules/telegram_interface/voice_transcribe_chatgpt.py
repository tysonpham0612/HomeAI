import os  # Import os module to work with files (delete downloaded file later)
from telegram import Update  # Update represents the incoming message from the user
from telegram.ext import ContextTypes  # ContextTypes is the context for managing conversations (standard with telegram.ext)
from services.whisper_client import transcribe_voice
from services.openai_client import get_chatgpt_response


# Define an asynchronous function that handles incoming voice messages
async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
     # Step 1: Download the voice file
    voice = update.message.voice
    voice_file = await voice.get_file()
    
    file_path = "received_voice.ogg"
    await voice_file.download_to_drive(file_path)
    
    try:
        # Step 2: Transcribe voice to text
        transcribed_text = await transcribe_voice(file_path)

        #Step 3: Send transcribed text to ChatGPT
        user_id = update.message.from_user.id
        chat_response = await get_chatgpt_response(user_id,transcribed_text)

        #Step 4: Reply back with ChatGPT's smart response
        await update.message.reply_text(chat_response)

    except Exception as e:
        await update.message.reply_text("Sorry, I couldn't understand your voice message.")
        print(f"Voice handling error: {e}")

    finally:
        # Always clean up temporary file
        if os.path.exists(file_path):
            os.remove(file_path)
