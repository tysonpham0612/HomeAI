HomeAI (Luna) - Smart Home AI Assistant
Overview
HomeAI (Luna) is a modular, AI-powered smart home assistant designed to integrate seamlessly with Home Assistant OS. It leverages OpenAI's ChatGPT and Whisper for natural language understanding and voice transcription, enabling users to control smart devices, monitor their environment, and engage in natural conversations via Telegram.

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

Usage
Telegram Commands
/start: Start the bot and receive a welcome message.
/help: Display available commands and usage instructions.
/reset: Reset the conversation history.
Natural Language Interaction
Send text or voice messages to the bot for:
Controlling smart devices (e.g., "Turn on the kitchen lights").
Asking general questions (e.g., "What's the weather today?").
How It Works

1. Text Message Flow
   User Input: The user sends a text message to the bot.
   Processing:
   The message is handled by handle_text in text_chatgpt.py.
   It calls process_user_text in intent_dispatcher.py to:
   Append the message to the conversation history.
   Send the conversation to ChatGPT for processing.
   Parse the response to determine if it is a command or a natural reply.
   Command Execution:
   If it is a command, it is routed to Home Assistant via route_chatgpt_response in router.py.
   Response:
   The bot sends a confirmation or natural reply back to the user.
2. Voice Message Flow
   User Input: The user sends a voice message to the bot.
   Processing:
   The voice message is transcribed to text using Whisper in whisper_client.py.
   The transcribed text is processed as a regular text message.
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
   Credits
   Creator: Tyson Pham
   Location: Canada
   Special Note: Designed with care to be a practical and friendly assistant for daily living.
   Future Enhancements
   Add persistent storage for conversation history.
   Implement advanced error handling and logging.
   Add support for multiple AI models (e.g., Hugging Face).
   Extend functionality with additional smart home integrations.
