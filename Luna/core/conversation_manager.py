
# This file manages conversation history for each user.
# Store conversations in memory (simple dictionary for now)

from configs.assistant_profile import build_default_system_prompt
system_prompt = build_default_system_prompt("Luna")

user_conversations = {}
def get_conversation(user_id:int)->list:
    
    # Get the conversation history for a user.
    # If user doesn't exist, create a new conversation.
    
    if user_id not in user_conversations:
        user_conversations[user_id] = [
            {"role": "system", "content": system_prompt}
        ]
    return user_conversations[user_id]


def append_user_message(user_id: int, message: str):
    # Add a new user message to the conversation.
    conversation = get_conversation(user_id)
    conversation.append({"role":"user","content":message})

def append_bot_message(user_id: int, message: str):
    # Add a new assistant (bot) message to the conversation.

    conversation = get_conversation(user_id)
    conversation.append({"role": "assistant", "content": message})

def clear_conversation(user_id: int):

    # Clears the conversation history for a user (optional feature later).
    
    if user_id in user_conversations:
        del user_conversations[user_id]
