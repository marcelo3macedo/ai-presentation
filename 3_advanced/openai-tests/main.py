import openai, os
from dotenv import load_dotenv

load_dotenv()

audio_file= open("audio.mp3", "rb")
openai.api_key = os.getenv('OPENAI_KEY')

transcript = openai.Audio.transcribe("whisper-1", audio_file)

print(transcript)