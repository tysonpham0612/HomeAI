from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__),'.env')
load_dotenv(dotenv_path = dotenv_path)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
BOT_TOKEN = os.getenv("BOT_TOKEN")
