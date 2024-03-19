from transformers import pipeline
import json

# Load the model
unmasker = pipeline('fill-mask', model='bert-base-uncased')

def predict(request):
    request_json = request.get_json(silent=True)
    sentence = request_json.get('sentence')

    if not sentence:
        return json.dumps({'error': 'No sentence provided'}), 400

    result = unmasker(sentence)
    return json.dumps({'result': result})
