import config
import os
import azure.cognitiveservices.speech as speechsdk

def text_to_speech(text):
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=config.AzureSpeechKey, endpoint=config.AzureEndpoint)
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    # SSML text
    ssml_text = f"""
        <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
            <voice name="en-US-AriaNeural">
                <mstts:express-as style="friendly">
                    {text}
                </mstts:express-as>
            </voice>
        </speak>"""

    ## Calling the Speech Sythesizer
    speech_synthesizer.speak_ssml_async(ssml=ssml_text).get()

