#This file makes logic based on returned response of chatgpt
from core.conversation_manager import append_user_message,append_bot_message
from services.openai_client import get_chatgpt_response
from core.intent_parser import parse_intent
from core.router import route_chatgpt_response

async def process_user_text(user_id:int, user_message:str) -> str:
    #  """
    # Process a user's text input by:
    # 1. Appending the message to conversation history
    # 2. Sending the full history to ChatGPT for analysis
    # 3. Parsing the GPT response into intent components
    # 4. Routing the command to Home Assistant if it's actionable
    # 5. Returning a reply string for the bot to send back to the user

    # Args:
    #     user_id (int): Telegram user ID
    #     user_input (str): Text message sent by the user

    # Returns:
    #     str: Text response to be sent back to the user
    # """
     
     # 1. Add user's message to conversation memory
    append_user_message(user_id, user_message)

    # 2. Send full history to ChatGPT and get structured JSON-like response
    gpt_response = await get_chatgpt_response(user_id, user_message)

    # 3. Parse GPT response into components
    is_command, action, target, reply, confidence = parse_intent(gpt_response)

    # 4. If it's not a command (just a normal chat reply), return it directly
    if not is_command:
        append_bot_message(user_id, reply)
        return reply

    # 5. If it's a command, route it to Home Assistant (via router logic)
    result = route_chatgpt_response({
        "action": action,
        "target": target
    })

    # 6. Save the assistant's command response and return it
    append_bot_message(user_id, result)
    return result