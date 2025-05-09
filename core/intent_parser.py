import json

def parse_intent(gpt_output: str):
    """
    Parses a JSON-formatted string returned by ChatGPT and extracts structured intent.

    Args:
        gpt_output (str): GPT's response in JSON format

    Returns:
        tuple: (is_command, action, target, reply, confidence)
    """

    try:
        data = json.loads(gpt_output)
    except json.JSONDecodeError:
        # Fallback if GPT gave plain text or invalid JSON
        return False, None, None, gpt_output, 1.0

    #value = data.get("key", default_value)
    return (
        data.get("is_command", False),   # Whether GPT thinks this is a command
        data.get("action"),              # Action to perform (e.g. "turn_on")
        data.get("target"),              # Device or entity (e.g. "light.kitchen")
        data.get("reply"),               # Reply message for the user
        data.get("confidence", 1.0)      # Confidence score (optional)
    )