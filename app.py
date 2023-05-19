from flask import Flask, render_template, request, jsonify
import subprocess

import InputOutput
import speech_recognition

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/start-recording', methods=['POST'])
def start_recording():
    # Call the separate Python file to stop audio recording and process the recorded audio
    result = speech_recognition.recognize_from_microphone()
    print(result)
    return result


if __name__ == '__main__':
    app.run()
