from flask import Flask, jsonify, render_template
from EmotionDetector.emotion_detector import emotion_detector
app=Flask(__name__)


@app.route("/emotionalDetector")
def sent_analyzer():
    # Necesitas devolver el resultado del análisis
    result = emotion_detector('Me encanta esta nueva tecnología.')
    return jsonify(result)

@app.route("/")
def render_index_page():
    return render_template('index.html')




if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)