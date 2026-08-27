from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_route():
    # Obtener el texto del parámetro de la URL
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Llamar a la función emotion_detector
    response = emotion_detector(text_to_analyze)
    
    # Formatear la respuesta
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    # Crear la respuesta formateada
    formatted_response = f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    
    return formatted_response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
