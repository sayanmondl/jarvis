from pathlib import Path

def text_to_speech(client, text):
    speech_response = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=text
    )
    speechfile_path = Path(__file__).parent / "speeches/speech.mp3"
    speech_response.stream_to_file(speechfile_path)


def speech_to_text(client, speechfile_path) -> str:
    audiofile = open(speechfile_path, "rb")
    text_output = client.audio.transcriptions.create(
        model="whisper-1",
        file=audiofile
    )
    return text_output.text
