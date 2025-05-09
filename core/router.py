from services.ha_client import send_ha_command

def route_chatgpt_reply(intent_dict: dict, force_execute: bool = False) -> str:
    """
    Routes a parsed intent to Home Assistant by constructing the correct
    domain/service/entity command and calling the HA client.

    Args:
        intent_dict (dict): Must include 'action' and 'target'
        force_execute (bool): Bypass confirmation step if set

    Returns:
        str: Text response to confirm the action was executed
    """

    action = intent_dict["action"]            # e.g. "turn_off"
    target = intent_dict["target"]            # e.g. "light.kitchen"
    domain = target.split(".")[0]             # e.g. "light"
    service = action.lower()                  # HA expects lowercase service names

    # Send command to Home Assistant API
    send_ha_command(domain, service, target)

    # Return confirmation message
    return f"✅ {target.replace('_', ' ')} has been {service.replace('_', ' ')}."