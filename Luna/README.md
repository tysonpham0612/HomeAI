Welcome to Luna, the Smart Home AI Assistant Bot!
This project connects a Telegram bot to OpenAI's ChatGPT API, allowing natural conversation without rigid commands.
It is built to be modular, scalable, and professional — ready to add Smart Home features, image recognition, voice transcription, and more.

🚀 Features
/start — Welcome message.

/help — Shows available features.

Normal text chatting — No commands needed, just talk naturally.

Voice message handling — Send a voice recording, bot echoes it back.

Fully modular structure — Easy to add new services like Image AI, Voice-to-Text AI later.

Scalable — Clean separation between handlers (interaction) and services (processing).

HomeAI/
├── .venv/ # Your virtual Python environment (isolated libraries)
├── bot/ # All your actual project code
│ ├── **init**.py # (Makes this folder a Python package)
│ ├── main.py # (Entry point to start the bot)
│ ├── config.py # (All your secret API keys and settings)
│ ├── handlers/ # (All code that reacts to messages)
│ │ ├── start.py
│ │ ├── help.py
│ │ ├── text_chatgpt.py
│ │ └── voice_echo.py
│ ├── services/ # (All code that calls external AI models or APIs)
│ ├── chatgpt_service.py
│ ├── image_recognition_service.py (future)
├── requirements.txt # (List of libraries you need)
└── README.md # (Documentation about your project)

🛠️ How to Run

1. Clone the project (or set up your folder manually).

2. Create a .venv and activate it.
   python3 -m venv .venv
   source .venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4.Set up your API keys in bot/config.py:
BOT_TOKEN = "your-telegram-bot-token"
OPENAI_API_KEY = "your-openai-api-key"

5.Run the bot:
./.venv/bin/python bot/main.py
✅ Bot will print Bot is running... when successful.

✨ How Handlers and Services are Separated
Handlers deal with user inputs (text, voice, photo).

Services deal with external AI processing (ChatGPT, Image Recognition, Voice Transcription).

This separation makes it easy to add new features without touching unrelated code.

🛤️ Scalability Example
In the future, you can add:

Chat with ChatGPT ✅ (already done)

Analyze uploaded images using DALL-E or Vision AI ✅ (add image_recognition_service.py)

Transcribe voice recordings to text using Whisper ✅ (add voice_to_text_service.py)

WITHOUT touching main.py too much.

Just:

Add a new service in services/

Add a new handler in handlers/

Connect them briefly in main.py

✅ Your architecture is already ready for smart home commands, AI recognition, security detection, and more.

🧠 Core Responsibilities
bot/main.py — Starts the app, connects all handlers.

bot/config.py — Stores API keys and settings.

bot/handlers/ — Handles user interactions like text, voice, commands.

bot/services/ — Processes AI tasks like calling ChatGPT or Vision models.

.venv/ — Keeps dependencies isolated.

requirements.txt — Easy installation of all needed Python libraries.

📢 Important Notes
Protect your API keys!
Never upload config.py to GitHub unless you remove or hide your real API keys.

Check OpenAI billing — API usage is paid after the free trial.

Modularity is key — Always add new features as separate service/handler files.

🎯 Future Roadmap Ideas
🔥 Add Smart Home control commands ("Turn on lights", "Lock the door").

🔥 Add Image Recognition (object detection in photos).

🔥 Add Voice-to-Text transcription.

🔥 Add Memory (store user preferences).

🔥 Add Inline Buttons (Telegram keyboards).
