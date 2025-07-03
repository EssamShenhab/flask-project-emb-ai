"""Flask web server for the Emotion Detection application."""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """Render the homepage with the input form."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def get_emotion():
    """Process the user input and return the detected emotions."""
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return "Invalid text! Please try again!"

    emotions = emotion_detector(text_to_analyze)

    if emotions['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, "
        f"'joy': {emotions['joy']} and "
        f"'sadness': {emotions['sadness']}. "
        f"The dominant emotion is {emotions['dominant_emotion']}."
    )

    return response_text

if __name__ == '__main__':
    app.run(debug=True)
