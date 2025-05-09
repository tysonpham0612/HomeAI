Documentation for HomeAI (Luna)
Overview
HomeAI (Luna) is a modular, AI-powered smart home assistant designed to integrate with Home Assistant OS. It leverages advanced AI technologies like OpenAI's ChatGPT and Whisper for natural language understanding and voice transcription. Luna provides a seamless interface for controlling smart home devices, monitoring the environment, and engaging in natural conversations via platforms like Telegram.

Features
AI Assistant: ChatGPT-powered assistant with memory for natural language interaction.
Voice Transcription: Converts voice messages to text using OpenAI's Whisper.
Home Automation: Integrates with Home Assistant to control devices and monitor the environment.
Telegram Integration: Two-way interaction via Telegram for text and voice commands.
Extensibility: Modular architecture for adding new AI capabilities like object detection or image recognition.
REST API Control: Communicates with Home Assistant via its REST API for device control.
Project Structure

1. Main Entry Point
   main.py: Initializes the Telegram bot, registers command and message handlers, and starts the webhook server.
2. Core Logic
   core: Contains the brain of the application, including conversation memory, intent parsing, and routing logic.
   conversation_manager.py: Manages user conversations and stores them in memory.
   intent_dispatcher.py: Processes user input, determines intent, and routes commands.
   intent_parser.py: Parses ChatGPT's JSON responses into actionable intents.
   router.py: Routes parsed intents to Home Assistant for execution.
3. Services
   services: Handles third-party integrations like OpenAI and Home Assistant.
   openai_client.py: Communicates with OpenAI's ChatGPT and Whisper APIs.
   whisper_client.py: Handles voice transcription using Whisper.
   ha_client.py: Sends commands to Home Assistant via its REST API.
4. Modules
   modules: Contains self-contained interface modules for different functionalities.
   telegram_interface/: Handles Telegram bot commands and messages.
   start.py: Responds to the /start command.
   help.py: Provides help information via the /help command.
   reset.py: Resets the conversation history with the /reset command.
   text_chatgpt.py: Processes text messages using ChatGPT.
   voice_transcribe_chatgpt.py: Processes voice messages using Whisper and ChatGPT.
   webhook_interface/: Implements a FastAPI server for receiving webhooks (e.g., motion detection).
5. Configuration
   configs: Stores environment variables and assistant profile settings.
   config.py: Loads API keys and tokens from a .env file.
   assistant_profile.py: Defines the assistant's personality, abilities, and behavior rules.
6. Tests
   tests: (Optional) Contains test files for validating services and core logic.
   Setup Instructions
7. Clone the Repository
8. Create a Virtual Environment
9. Install Dependencies
10. Configure Environment Variables
    Create a .env file in the project root with the following content:

11. Run the Application
    Usage
    Telegram Commands
    /start: Start the bot and receive a welcome message.
    /help: Display available commands and usage instructions.
    /reset: Reset the conversation history.
    Natural Language Interaction
    Send text or voice messages to the bot for:
    Controlling smart devices (e.g., "Turn on the kitchen lights").
    Asking general questions (e.g., "What's the weather today?").
    Extending the Application
    Adding a New Module
    Create a new folder in modules (e.g., modules/image_recognition/).
    Implement the module's logic.
    Update the router or relevant handlers to integrate the new module.
    Example: Adding Object Detection
    Use YOLO or another object detection library.
    Create a new module for processing images and returning detected objects.
    Route image-related commands to this module.
    Deployment
    Run at Boot: Use a script like start_bot.sh or configure a crontab entry.
    Docker Support: (Coming soon) Containerize the application for easier deployment.
    Remote Access: Use Home Assistant's DuckDNS and HTTPS for secure remote access.
    Notes
    Ensure Home Assistant is running on the same network.
    Register ESP32 devices via MQTT or ESPHome for seamless integration.
    Prioritize local-first design for privacy and security.
    Credits
    Creator: Thai Son Pham
    Location: Canada
    Special Note: Designed with care to be a practical and friendly assistant for daily living.
