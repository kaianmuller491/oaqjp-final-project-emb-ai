"""
Flask server for emotion detection.

This module provides a REST API to analyze emotions in a given text

 using the EmotionDetector library.
"""

from flask import Flask, jsonify, request, render_template
from EmotionDetector.emotion_detector import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyzes the emotion of the provided text.

    Returns:
        JSON: A JSON object containing the emotion analysis result or an error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 200

    return jsonify(result)

@app.route("/")
def render_index_page():
    """
    Renders the index page.

    Returns:
        HTML: The rendered index.html template.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
