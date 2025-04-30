import openai
from configs.config import OPENAI_API_KEY
openai.api_key = OPENAI_API_KEY

async def transcribe_voice(file_path:str)->str:
    with open(file_path, 'rb') as audio_file:
        transcript =  openai.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return transcript.text
