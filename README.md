Luna

Home AI Hub (Luna) is a modular, AI-powered smart home assistant designed to integrate with Home Assistant OS. It connects multiple intelligent modules like ChatGPT, Whisper (voice-to-text), and YOLO (object detection), enabling users to control and monitor their smart home via platforms like Telegram or future custom interfaces.

---

✨ Features

- ChatGPT-driven AI assistant ("Luna") with memory
- Telegram integration for two-way natural language interaction
- Voice transcription with Whisper
- Object detection support via YOLO (extensible)
- REST API control of Home Assistant (switches, sensors, scenes)
- Plug-and-play architecture for adding or removing AI modules

---

🧱 Project Structure

main.py  
Entry point that loads configuration, starts the router, and launches the primary interface (Telegram, etc.).

core/  
Houses the brain logic, conversation memory, intent parsing, and routing between modules.

services/  
Handles all third-party integrations like OpenAI, Whisper API, MQTT, and Home Assistant REST API.

modules/  
Self-contained interface modules like telegram_interface, whisper_transcriber, ha_connector, and more.

configs/  
Stores environment loading and secrets config logic (e.g., tokens, URLs).

tests/  
Optional test files for validating services and core logic.

---

⚙️ Setup

1. Clone this repository

2. Create a virtual environment

   python3 -m venv venv
   source venv/bin/activate

3. Install dependencies

   pip install -r requirements.txt

4. Create a .env file in the project root:

   BOT_TOKEN=your_telegram_bot_token
   OPENAI_API_KEY=your_openai_key
   HA_TOKEN=your_home_assistant_token
   HA_URL=

5. Run the assistant

   python main.py

---

🔌 Add a New Module

To add new AI capability (e.g., face recognition, image captioning), create a folder in modules/, write its logic, and update the router to route relevant inputs.

Modules are hot-swappable and do not require changes to core logic if you follow the existing interface patterns.

---

🚀 Deployment

- Use start_bot.sh to run the project at boot or via crontab
- Docker support coming soon for full containerization
- Remote access supported via Home Assistant + DuckDNS + HTTPS

---

📌 Notes

- This project assumes Home Assistant OS is running on the same network
- All ESP32 devices should be registered via MQTT or ESPHome and managed by HA
- This is a local-first design with optional remote features

---

🤖 Credits

Built by Thai Son Pham as a personal AI smart home framework.
