from transformers import WhisperProcessor, WhisperForConditionalGeneration
from transformers import pipeline
from pathlib import Path
from typing import Tuple


SAVED_MODEL_PATH = "../flask"
PROCESSOR_PATH = str(Path(SAVED_MODEL_PATH, "processor.h5"))
VOICE2TEXT_PATH = str(Path(SAVED_MODEL_PATH, "voice2text.h5"))
PARAPHRASER_PATH = str(Path(SAVED_MODEL_PATH, "paraphraser.h5"))


def load_paraphraser() -> pipeline:
    """
    This function load text2text paraphraser model and returns it
    """
    paraphraser = pipeline("text2text-generation", model="humarin/chatgpt_paraphraser_on_T5_base")
    return paraphraser


def load_voice2text() -> Tuple[WhisperProcessor, WhisperForConditionalGeneration]:
    """
    This function loads voice2text model and returns it.

    :return: processor and voice2text model
    """
    # load model and processor
    processor = WhisperProcessor.from_pretrained("openai/whisper-tiny")
    voice2text_model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-tiny")
    voice2text_model.config.forced_decoder_ids = None

    return processor, voice2text_model


if __name__ == "__main__":
    processor, voice2text_model = load_voice2text()
    paraphraser = load_paraphraser()

    # save models locally
    processor.save_pretrained(PROCESSOR_PATH)
    voice2text_model.save_pretrained(VOICE2TEXT_PATH)
    paraphraser.save_pretrained(PARAPHRASER_PATH)

