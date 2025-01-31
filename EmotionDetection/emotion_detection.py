import requests
import json

# emotion detector function
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_data = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = json_data, headers = headers )

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
            }

    formatted_response = response.json()
    emotion_scores = formatted_response["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotion_scores, key = emotion_scores.get)

    return {
            'anger': emotion_scores["anger"],
            'disgust': emotion_scores["disgust"],
            'fear': emotion_scores["fear"],
            'joy': emotion_scores["joy"],
            'sadness': emotion_scores["sadness"],
            'dominant_emotion': dominant_emotion
            }
