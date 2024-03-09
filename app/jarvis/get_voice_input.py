import pyaudio
import wave
import threading

class AudioRecorder():
    def __init__(self):
        self.audio = pyaudio.PyAudio()
        self.is_recording = False
        self.stream = None
        self.frames = []

    def record_audio(self, startButton, executeButton):
        self.is_recording = True
        self.frames = []
        startButton.setEnabled(False)
        executeButton.setEnabled(True)

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

    def stop_recording(self, startButton, executeButton):
        if self.stream:
            self.is_recording = False
            self.recording_thread.join()

            self.stream.stop_stream()
            self.stream.close()
            self.audio.terminate()

            wf = wave.open("output.wav", "wb")
            wf.setnchannels(1)
            wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
            wf.setframerate(44100)
            wf.writeframes(b"".join(self.frames))
            wf.close()

            startButton.setEnabled(True)
            executeButton.setEnabled(False)