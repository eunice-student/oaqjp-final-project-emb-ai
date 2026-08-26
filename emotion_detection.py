import requests
import json

def emotion_detector(text_to_analyze):
    """
    Function to detect emotions from text using Watson NLP library
    """
    # URL del servicio de Watson NLP
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers requeridos
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Input JSON format
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Enviar POST request
    response = requests.post(url, headers=headers, json=input_json)
    
    # Retornar el atributo 'text' de la respuesta
    return response.text
