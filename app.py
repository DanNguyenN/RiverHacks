from flask import Flask, render_template, request, jsonify
import subprocess
import threading

import InputOutput
import speech_recognition
import ChatGPT
import text_to_speech


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/start-recording', methods=['POST'])
def start_recording():
    # Call the separate Python file to stop audio recording and process the recorded audio
    result = speech_recognition.recognize_from_microphone()
    print(result)
    return jsonify({'status': 'success', 'userInput': result})

@app.route('/process-text', methods=['POST'])
def process_text():
    data = request.json
    text = data.get('user_input')
    response = ChatGPT.chat_gpt(text)

    def perform_text_to_speech():
        audio_data = text_to_speech.text_to_speech(response)
        # Code to save or send the audio data as needed

    thread = threading.Thread(target=perform_text_to_speech)
    thread.start()

    return jsonify({'status': 'success', 'userInput': response})


if __name__ == '__main__':
    app.run()
