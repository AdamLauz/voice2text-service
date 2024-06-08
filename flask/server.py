import random
import os
from flask import Flask, request, jsonify
from voice2text_service import voice2text_service

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    # get audio file and save it
    audio_file = request.files["file"]
    use_paraphrasing = request.form.get("use_paraphrasing")
    file_name = str(random.randint(0, 100000))
    audio_file.save(file_name)

    # invoke voice2text service
    voice2text = voice2text_service()

    # make a prediction
    transcription = voice2text.predict(file_name, use_paraphrasing=use_paraphrasing)

    # remove the audio file
    os.remove(file_name)

    # send back the predicted keyword in json format
    data = {"transcription": transcription}
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=False)
