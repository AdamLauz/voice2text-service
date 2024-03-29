# Voice2Text Web Service

This project is a web service built using Flask, Python, Nginx, and Docker, aimed at converting voice input to text using trained models.


based on [[1]](#1) by Valerio Velardo.


## Project Structure

```css
voice2text/
│
├── flask/
│   ├── paraphraser.h5/
│   ├── processor.h5/
│   ├── voice2text.h5/
│   ├── app.ini
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── server.py
│   ├── voice2text_service.py
│   
├── model/
│   ├── model.py
│   
├── nginx/
│   ├── Dockerfile
│   ├── nginx.conf
│   
├── resources/
│   ├── down.wav
│   ├── I had some free time, so I wandered around town.mp3
│   ├── People living in town don't know the pleasures of country life.mp3
│   
├── client.py
└── docker-compose.yml
```



## Description
Convert audio to text by calling this service. Ability to paraphrase the transcribed text using chatgpt paraphraser. 

## Transformers (Models Used)
The service utilizes pre-trained models for voice-to-text conversion. These models are based on the Hugging Face Transformers library and include:

1. [Whisper](https://huggingface.co/docs/transformers/model_doc/whisper) for voice-to-text transformation
2. [ChatGPT Paraphraser](https://huggingface.co/humarin/chatgpt_paraphraser_on_T5_base) for paraphrasing

For details on the models' architecture and training, refer to the respective model documentation.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/AdamLauz/voice2text.git
   cd voice2text
   ```

2. Install Docker:
Follow the official Docker installation guide for your operating system.

3. Build Docker images and start containers:
```bash
docker-compose up --build
```

## Usage
Once the Docker containers are running:
1. Use the provided client.py script to send audio files for transcription. The service supports both WAV and MP3 formats.
```bash
python client.py
```
2. Check the console output for the transcribed text.

## API Endpoint
The API endpoint for transcribing audio files is:
```bash
http://localhost:80/predict
```

## Architecture and How It Works
The web service architecture consists of three main components:

* Flask Server: Handles incoming HTTP requests, processes audio files, and invokes the voice-to-text service.
* Voice-to-Text Service: Utilizes trained models to convert audio input into text.
* Nginx Reverse Proxy: Routes requests from clients to the Flask server.

When a client sends an audio file to the /predict endpoint, the Flask server:

1. Saves the audio file locally.
2. Invokes the voice-to-text service to generate a transcription.
3. Sends back the transcribed text as a JSON response.

## Example Call (Replace with Real Example)
Below is an example of how to call the service using cURL:
```bash
curl -X POST -F "file=@/path/to/your/audio/file.mp3" http://localhost:80/predict
```
Replace /path/to/your/audio/file.mp3 with the path to your actual audio file in MP3 format.

## Additional Notes
* The Flask server is exposed on port 900 within the Docker network.
* Nginx is used as a reverse proxy to route requests to the Flask server.
* Make sure to provide audio files in WAV or MP3 format for transcription.

## Troubleshooting
* If you encounter any issues, check the Docker logs for the Flask and Nginx containers.
* Ensure that the required dependencies are installed as specified in requirements.txt.

## References
<a id="1">[1]</a>
Valerio Velardo.
https://github.com/musikalkemist/Deep-Learning-Audio-Application-From-Design-to-Deployment
