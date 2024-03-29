# voice2text-service
voice2text nginx &amp; flask service based on Whisper and ChatGPT paraphraser transformers.
The web service has a predict endpoint which can get a file using a POST call. The service uses Whisper to transcribe the audio speach and then the ChatGPT paraphraser is used to generate paraphrase. The service returns the paraphreasesd text. 

based on [[1]](#1) by Valerio Velardo.

## Description
Convert audio to text by calling this service. Ability to paraphrase the transcribed text using chatgpt paraphraser. 

## Transformers
1. [Whisper](https://huggingface.co/docs/transformers/model_doc/whisper)
2. [ChatGPT Paraphraser](https://huggingface.co/humarin/chatgpt_paraphraser_on_T5_base)

## References
<a id="1">[1]</a>
Valerio Velardo.
https://github.com/musikalkemist/Deep-Learning-Audio-Application-From-Design-to-Deployment
