import librosa
from pathlib import Path
from transformers import WhisperProcessor, WhisperForConditionalGeneration
from transformers import pipeline

PROCESSOR_PATH = str(Path("processor.h5"))
VOICE2TEXT_PATH = str(Path("voice2text.h5"))
PARAPHRASER_PATH = str(Path("paraphraser.h5"))
SAMPLING_RATE = 16000


class _Voice2TextService:
    """
    Singleton class for voice to text transformation using trained models
    """
    _instance = None

    processor = None
    voice2text = None
    paraphraser = None

    def predict(self, file_path: str, use_paraphrasing: bool = False):
        """

        :param use_paraphrasing:
        :param file_path:
        :return:
        """
        # preprocess
        input_features = self.preprocess(file_path=file_path)

        # generate token ids
        predicted_ids = self.voice2text.generate(input_features)

        # decode token ids to text
        transcription = self.processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]

        # use paraphrasing
        if use_paraphrasing:
            transcription = (f"paraphrase: {transcription[0]}")

        return transcription

    def preprocess(self, file_path: str):
        """
        This method loads an audio file from file_path and uses the preprossor model
        to convert the audio data into features that can be used as input to the voice2text model
        :param file_path:
        :return:
        """
        # Loading the audio file
        audio_data, rate = librosa.load(file_path, sr=SAMPLING_RATE)

        input_features = self.processor(audio_data, sampling_rate=SAMPLING_RATE,
                                       return_tensors="pt").input_features
        return input_features

    @property
    def instance(self):
        return self._instance


def voice2text_service():
    """
    Factory function for _Voice2TextService class
    """
    if _Voice2TextService._instance is None:
        _Voice2TextService._instance = _Voice2TextService()
        _Voice2TextService.processor = WhisperProcessor.from_pretrained(PROCESSOR_PATH)
        _Voice2TextService.voice2text = WhisperForConditionalGeneration.from_pretrained(VOICE2TEXT_PATH)
        _Voice2TextService.paraphraser = pipeline("text2text-generation", model=PARAPHRASER_PATH)

    return _Voice2TextService._instance


if __name__ == "__main__":
    voice2text = voice2text_service()
    voice2text_2 = voice2text_service()

    assert voice2text is voice2text_2

    # make prediction
    transcription = voice2text.predict("../resources/down.wav")
    print(transcription)
