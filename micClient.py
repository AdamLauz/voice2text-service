import requests
import pyaudio
import wave
import queue
import threading

URL = "http://127.0.0.1/predict"

CHUNK = 1024  # Size of each audio chunk
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100  # Sample rate (you can adjust this)
RECORD_SECONDS = 3  # Duration of each recording

# Queue to store audio chunks
audio_queue = queue.Queue()


def record_audio():
    """Function to continuously record audio from the microphone and store it in the queue."""
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    print("Recording...")

    while True:
        frames = []
        for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        audio_queue.put(b''.join(frames))


def process_audio(use_paraphrasing: bool = False):
    """Function to continuously read audio chunks from the queue and send them to the service."""
    while True:
        audio_data = audio_queue.get()
        # Save the audio to a temporary WAV file
        temp_wav_file = "temp_audio.wav"
        with wave.open(temp_wav_file, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(pyaudio.PyAudio().get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(audio_data)

        # Send the recorded audio to the local service
        with open(temp_wav_file, "rb") as audio_file:
            values = {"file": ("temp_audio.wav", audio_file, "audio/wav")}
            response = requests.post(URL, files=values, data={'use_paraphrasing': use_paraphrasing})
            data = response.json()

        print(f"Transcribed {'and paraphrased' if use_paraphrasing else ''} text is: {data['transcription']}")


if __name__ == "__main__":
    # Start recording audio in a separate thread
    record_thread = threading.Thread(target=record_audio)
    record_thread.daemon = True
    record_thread.start()

    # Process audio in the main thread
    process_audio(use_paraphrasing=False)
