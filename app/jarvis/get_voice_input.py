import pyaudio
import wave
import threading


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

    def stop_recording(self):
        if self.stream:
            self.is_recording = False
            self.recording_thread.join()

            wf = wave.open(f"data/audio/output_{self.record_index}.wav", "wb")
            wf.setnchannels(1)
            wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
            wf.setframerate(44100)
            wf.writeframes(b"".join(self.frames))
            wf.close()

            self.start_buttton.setEnabled(True)
            self.stop_button.setEnabled(False)
