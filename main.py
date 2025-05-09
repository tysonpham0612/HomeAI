# Telegram imports
import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
#Webhook imports
from modules.webhook_interface.webhook_server import start_webhook_server
#config imports
from configs.config import BOT_TOKEN
#Module command imports
from modules.telegram_interface.start import start
from modules.telegram_interface.help import help_command
from modules.telegram_interface.reset import reset
#Module message imports
from modules.telegram_interface.text_chatgpt import handle_text
from modules.telegram_interface.voice_transcribe_chatgpt import handle_voice

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    #Register command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("reset", reset))
    #Register message handlers
    app.add_handler(MessageHandler(filters.VOICE, handle_voice))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
    start_webhook_server()
