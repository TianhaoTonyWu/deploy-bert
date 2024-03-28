import os
from flask import Flask, request, jsonify
from transformers import pipeline
import time


app = Flask(__name__)

# Load the model
unmasker = pipeline('fill-mask', model='bert-base-uncased')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    sentence = data.get('sentence')
    if not sentence:
        return jsonify({'error': 'No sentence provided'}), 400

    start_time = time.time()
    result = unmasker(sentence)
    end_time = time.time()

    response_time = end_time - start_time

    return jsonify({'result': result, 'response_time': response_time})



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))