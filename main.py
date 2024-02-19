from openai import OpenAI
from dotenv import load_dotenv
import text_speech_conversion
import os

load_dotenv()
api_key = os.getenv("OPENAI_KEY")
client = OpenAI(api_key=api_key)

textinput = "A quick brown fox jumps over a lazy dog"
text_speech_conversion.text_to_speech(textinput)

print()