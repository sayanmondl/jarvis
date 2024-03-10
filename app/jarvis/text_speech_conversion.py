from pathlib import Path

def text_to_speech(client, text, outputfile_path):
    speech_response = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=text
    )
    speech_response.stream_to_file(outputfile_path)


def speech_to_text(client, speechfile_path) -> str:
    audiofile = open(speechfile_path, "rb")
    text_output = client.audio.transcriptions.create(
        model="whisper-1",
        file=audiofile
    )
    return text_output.text
