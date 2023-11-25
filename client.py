import requests

URL = "http://127.0.0.1/predict"
TEST_AUDIO_FILE_PATH = "resources/left.wav"

if __name__ == "__main__":

    audio_file = open(TEST_AUDIO_FILE_PATH, "rb")
    values = {"file": (TEST_AUDIO_FILE_PATH, audio_file, "audio/wav")}
    response = requests.post(URL, files=values)
    data = response.json()

    print(f"Transcribed text is: {data['transcription']}")
