from openai import OpenAI
from dotenv import load_dotenv
from text_speech_conversion import *
import os

load_dotenv()
api_key = os.getenv("OPENAI_KEY")
client = OpenAI(api_key=api_key)

audiofile = open("D:/Projects/jarvis/app/jarvis/output.wav", "rb")
text = speech_to_text(client, audiofile)

print(text)