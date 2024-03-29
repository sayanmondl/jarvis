import pyaudio
import wave
import threading
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl
from jarvis.text_speech_conversion import *
from jarvis.completion import get_response
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_KEY")
client = OpenAI(api_key=api_key)

class AudioRecorder:
    def __init__(self, start_buttton, stop_button):
        self.audio = pyaudio.PyAudio()
        self.is_recording = False
        self.stream = None
        self.frames = []
        self.start_buttton = start_buttton
        self.stop_button = stop_button
        self.start_buttton.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.record_index = 0
        self.displaytext = ""
        self.audio_output = QAudioOutput()
        self.media_player = QMediaPlayer()

    def record_audio(self):
        self.is_recording = True
        self.frames = []
        self.start_buttton.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.record_index += 1

        self.stream = self.audio.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=44100,
            input=True,
            frames_per_buffer=1024,
        )

        self.recording_thread = threading.Thread(target=self.record_audio_thread)
        self.recording_thread.start()

    def record_audio_thread(self):
        while self.is_recording:
            data = self.stream.read(1024)
            self.frames.append(data)

    def process(self):
        if self.stream:
            self.is_recording = False
            self.recording_thread.join()

            wf = wave.open(f"data/audio/input/input_{self.record_index}.wav", "wb")
            wf.setnchannels(1)
            wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
            wf.setframerate(44100)
            wf.writeframes(b"".join(self.frames))
            wf.close()

            user_text = self.get_text()
            response_text = get_response(client, user_text)
            self.displaytext = response_text

            text_to_speech(client, response_text, f"data/audio/output/output_{self.record_index}.wav")
            self.play_audio()

            self.start_buttton.setEnabled(True)
            self.stop_button.setEnabled(False)

    def play_audio(self):
        self.media_player.setAudioOutput(self.audio_output)
        self.media_player.setSource(QUrl(f"data/audio/output/output_{self.record_index}.wav"))
        self.media_player.play()

    def get_text(self):
        text = speech_to_text(client,f"data/audio/input/input_{self.record_index}.wav")
        return text
