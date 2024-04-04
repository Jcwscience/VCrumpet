import sys
import os


import streamlit as st
from translator import Translator
from xtts_live.xtts_live import TextToSpeech
import sounddevice as sd  # Import the sounddevice module for audio streaming



model_path = "/home/john/Documents/XTTS-v2/"  # Path to the model directory
speaker_wavs = "/home/john/Documents/Voices/voice.wav"  # Path to the speaker's audio file

output_samplerate = 48000  # Output audio sample rate

tts = TextToSpeech(model_path, speaker_wavs, output_samplerate, use_deepspeed=True, debug=False)

def stream_callback(outdata, frames, time, status):
    if status:
        print(status)  # Print any status messages received during audio streaming
    outdata[:] = tts.audio_buffer.get_samples(frames)  # Fill the output audio buffer with samples from the TextToSpeech instance


stream = sd.OutputStream(
    device=20,  # Specify the audio output device index
    samplerate=output_samplerate,  # Set the sample rate for audio streaming
    channels=1,  # Set the number of audio channels
    callback=stream_callback,  # Set the callback function for audio streaming
    finished_callback=tts.stop,  # Set the finished callback function to stop the TextToSpeech instance
    dtype='float32'  # Set the data type for audio samples
)

stream.start()  # Start the audio streaming


# Initialize the Translator and TextToSpeechSystem
translator = Translator()  # Assuming English to Japanese translation as default

language_codes = {
    "Passthrough": None,
    #"Spanish": "es",
    #"French": "fr",
    #"German": "de",
    #"Italian": "it",
    #"Portuguese": "pt",
    #"Polish": "pl",
    #"Turkish": "tr",
    #"Russian": "ru",
    #"Dutch": "nl",
    #"Czech": "cs",
    #"Arabic": "ar",
    #"Chinese": "zh",
    "Japanese": "ja",
    #"Hungarian": "hu",
    #"Korean": "ko",
    #"Hindi": "hi"
}

# Streamlit interface
st.title('Translator with Text-to-Speech')

input_text = st.text_area("Text to translate", "Hello, world!")
selected_language = st.selectbox("Translation Language", language_codes.keys())  # Extend this list as needed
if translator.model_name:
    st.write(f"Loaded model: {translator.model_name}")
else:
    st.write("No model loaded")

if st.button('Translate and Speak'):
    translator.target_language = language_codes[selected_language]
    translation = translator.translate(input_text)
    st.write(f"Translation: {translation}")
    tts.speak(translation)

if st.button('Exit'):
    tts.stop()
    stream.stop()
    st.stop()
