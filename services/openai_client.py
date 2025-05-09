# services/chatgpt/chatgpt_service.py

import openai
from configs.config import OPENAI_API_KEY
from core.conversation_manager import (
    get_conversation, append_user_message, append_bot_message
)

openai.api_key = OPENAI_API_KEY

async def get_chatgpt_response(user_id: int, user_input: str) -> str:
  
    """
    Sends the full conversation history (including system prompt) to OpenAI's API
    and returns the assistant's raw JSON-formatted response as a string.

    Args:
        user_id (int): The Telegram user ID
        user_input (str): The latest user message (already stored in memory)

    Returns:
        str: JSON-formatted string response from GPT (structured intent + reply)
    """
 
    # 1. Get the full conversation history for the user
    messages = get_conversation(user_id)

    # 2. Send it to OpenAI's ChatCompletion API
    response = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.5
    )

    # 3. Return the assistant's response as plain text
    return response.choices[0].message.content.strip()


async def summarize_conversation(messages: list)->str:
    # Summarizes a long list of chat messages into a short assistant-readable format.

    # Args:
    #     messages (list): Full conversation history including system, user, and assistant roles.

    # Returns:
    #     str: Summary text of the earlier part of the conversation.
    # """
    summary_prompt = [
        {"role": "system", "content": "You are an assistant that summarizes conversations for future AI context."},
        {"role": "user", "content": f"Summarize this conversation for context:\n{messages}"}
    ]

    response = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=summary_prompt,
        temperature=0.3,
        max_tokens = 300,
    )
    return response.choices[0].message.content.strip()
