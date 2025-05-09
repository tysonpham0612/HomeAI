import pytest
import sys
import os
from unittest.mock import AsyncMock, patch
from core.intent_dispatcher import process_user_text
from core.conversation_manager import (
    init_conversation,
    get_conversation,
    append_user_message,
    append_bot_message,
    clear_conversation,
    check_and_summarize_if_needed
)
from core.router import route_chatgpt_response



# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
@pytest.mark.asyncio
async def test_valid_command():
    """
    Test processing a valid command (e.g., "Turn on the kitchen lights").
    """
    user_id = 12345
    user_message = "Turn on the kitchen lights."

    # Mock dependencies
    with patch("services.openai_client.get_chatgpt_response", new_callable=AsyncMock) as mock_gpt_response, \
         patch("core.intent_parser.parse_intent") as mock_parse_intent, \
         patch("core.router.route_chatgpt_response") as mock_route_response:

        # Mock ChatGPT response
        mock_gpt_response.return_value = '{"is_command": true, "action": "turn_on", "target": "light.kitchen", "reply": "Turning on the kitchen lights."}'

        # Mock intent parsing
        mock_parse_intent.return_value = (True, "turn_on", "light.kitchen", "Turning on the kitchen lights.", 0.95)

        # Mock routing response
        mock_route_response.return_value = "✅ Kitchen lights have been turned on."

        # Call the function
        response = await process_user_text(user_id, user_message)

        # Assertions
        mock_gpt_response.assert_called_once_with(user_id, user_message)
        mock_parse_intent.assert_called_once_with(mock_gpt_response.return_value)
        mock_route_response.assert_called_once_with({"action": "turn_on", "target": "light.kitchen"})
        assert response == "✅ Kitchen lights have been turned on."


@pytest.mark.asyncio
async def test_non_command():
    """
    Test processing a non-command input (e.g., "How's the weather?").
    """
    user_id = 12345
    user_message = "How's the weather?"

    # Mock dependencies
    with patch("services.openai_client.get_chatgpt_response", new_callable=AsyncMock) as mock_gpt_response, \
         patch("core.intent_parser.parse_intent") as mock_parse_intent:

        # Mock ChatGPT response
        mock_gpt_response.return_value = '{"is_command": false, "reply": "The weather is sunny today."}'

        # Mock intent parsing
        mock_parse_intent.return_value = (False, None, None, "The weather is sunny today.", 1.0)

        # Call the function
        response = await process_user_text(user_id, user_message)

        # Assertions
        mock_gpt_response.assert_called_once_with(user_id, user_message)
        mock_parse_intent.assert_called_once_with(mock_gpt_response.return_value)
        assert response == "The weather is sunny today."


@pytest.mark.asyncio
async def test_irrelevant_command():
    """
    Test processing an irrelevant command (e.g., "Fly to the moon").
    """
    user_id = 12345
    user_message = "Fly to the moon."

    # Mock dependencies
    with patch("services.openai_client.get_chatgpt_response", new_callable=AsyncMock) as mock_gpt_response, \
         patch("core.intent_parser.parse_intent") as mock_parse_intent:

        # Mock ChatGPT response
        mock_gpt_response.return_value = '{"is_command": false, "reply": "I cannot help with that request."}'

        # Mock intent parsing
        mock_parse_intent.return_value = (False, None, None, "I cannot help with that request.", 1.0)

        # Call the function
        response = await process_user_text(user_id, user_message)

        # Assertions
        mock_gpt_response.assert_called_once_with(user_id, user_message)
        mock_parse_intent.assert_called_once_with(mock_gpt_response.return_value)
        assert response == "I cannot help with that request."


@pytest.mark.asyncio
async def test_history_over_maximum_length():
    """
    Test handling conversation history exceeding the maximum token limit.
    """
    user_id = 12345
    user_message = "Tell me something interesting."

    # Mock dependencies
    with patch("services.openai_client.get_chatgpt_response", new_callable=AsyncMock) as mock_gpt_response, \
         patch("services.openai_client.summarize_conversation", new_callable=AsyncMock) as mock_summarize:

        # Initialize conversation with a long history
        init_conversation(user_id)
        for i in range(60):  # Add 60 messages to exceed MAX_HISTORY_LENGTH
            append_user_message(user_id, f"Message {i}")

        # Mock summarization response
        mock_summarize.return_value = "Summary of earlier conversation."

        # Mock ChatGPT response
        mock_gpt_response.return_value = '{"is_command": false, "reply": "Here is something interesting!"}'

        # Call the function
        response = await process_user_text(user_id, user_message)

        # Assertions
        mock_summarize.assert_called_once()  # Ensure summarization was triggered
        mock_gpt_response.assert_called_once_with(user_id, user_message)
        assert response == "Here is something interesting."

        # Check that the conversation was summarized
        conversation = get_conversation(user_id)
        assert len(conversation) <= 50  # Ensure history was trimmed


def test_clear_conversation():
    """
    Test clearing the conversation history.
    """
    user_id = 12345

    # Initialize and add messages
    init_conversation(user_id)
    append_user_message(user_id, "Hello!")
    append_bot_message(user_id, "Hi there!")

    # Clear conversation
    clear_conversation(user_id)
    conversation = get_conversation(user_id)

    # Assertions
    assert len(conversation) == 1  # Only system prompt should remain