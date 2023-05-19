import ChatGPT
import speech_recognition
import text_to_speech

def main():
    text = speech_recognition.recognize_from_microphone()
    answer = ChatGPT.chat_gpt(text)
    print(answer)
    text_to_speech.text_to_speech(answer)


if __name__ == '__main__':
    main()