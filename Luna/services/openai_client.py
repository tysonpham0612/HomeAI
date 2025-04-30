# services/chatgpt/chatgpt_service.py

import openai
from configs.config import OPENAI_API_KEY
from core.conversation_manager import (
    get_conversation, append_user_message, append_bot_message
)

openai.api_key = OPENAI_API_KEY

async def get_chatgpt_response(user_id: int, user_input: str) -> str:
  
    # Get ChatGPT response, maintaining conversation context for each user.
 
    # Step 1: Update conversation with new user message
    append_user_message(user_id, user_input)

    # Step 2: Fetch conversation history
    conversation = get_conversation(user_id)

    # Step 3: Send full conversation history to ChatGPT
    response =  openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        temperature=0.7,
        max_tokens=300,
    )

    # Step 4: Extract bot reply
    bot_reply = response.choices[0].message.content.strip()

    # Step 5: Add bot reply to conversation history
    append_bot_message(user_id, bot_reply)

    return bot_reply
