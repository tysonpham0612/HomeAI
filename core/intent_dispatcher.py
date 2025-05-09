from core.conversation_manager import append_user_message, append_bot_message
from services.openai_client import get_chatgpt_response
from core.intent_parser import parse_intent
from core.router import route_chatgpt_response

async def process_user_text(user_id: int, user_message: str) -> str:
    """
    Main entry point for processing user text input.
    Handles conversation management, intent parsing, and command routing.

    Args:
        user_id (int): Telegram user ID
        user_message (str): Text message sent by the user

    Returns:
        str: Text response to be sent back to the user
    """
    # Step 1: Append the user's message to the conversation history
    await append_user_message(user_id, user_message)

    # Step 2: Get the response from ChatGPT
    gpt_response = await get_chatgpt_response(user_id, user_message)

    # Step 3: Handle the GPT response
    return await handle_gpt_response(user_id, gpt_response)


async def handle_gpt_response(user_id: int, gpt_response: str) -> str:
    """
    Handles the GPT response by parsing and routing it.

    Args:
        user_id (int): Telegram user ID
        gpt_response (str): Raw response from ChatGPT

    Returns:
        str: Text response to be sent back to the user
    """
    # Parse the GPT response into intent components
    is_command, action, target, reply, confidence = parse_intent(gpt_response)

    if not is_command:
        # If it's not a command, append the bot's reply and return it
        append_bot_message(user_id, reply)
        return reply

    # If it's a command, handle it
    return await handle_command(user_id, action, target)


async def handle_command(user_id: int, action: str, target: str) -> str:
    """
    Handles actionable commands by routing them to Home Assistant.

    Args:
        user_id (int): Telegram user ID
        action (str): Action to perform (e.g., "turn_on")
        target (str): Target entity (e.g., "light.kitchen")

    Returns:
        str: Confirmation message after executing the command
    """
    # Route the command to Home Assistant
    result = route_chatgpt_response({
        "action": action,
        "target": target
    })

    # Append the bot's response to the conversation history
    append_bot_message(user_id, result)
    return result