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

print(f"Available languages: {', '.join(language_codes.keys())}")
target_language = input("Enter target language or leave empty for passthrough: ")

while True:
    try:
        text = input("Enter text to translate: ")
        if text.lower() in language_codes.keys().lower() or text in language_codes.items() or text == "passthrough":
            lang = text.lower()
            if lang == "Passthrough":
                print("Passthrough mode enabled.")
            elif lang in language_codes.keys().lower():
                target_language = language_codes[lang]
                translator.load_model(target_language)
            else:
                translator.load_model(lang)
            
                
        else:
            tts.speak(translator.translate(text))
    except KeyboardInterrupt:
        tts.stop()
        stream.stop()
        stream.close()
        break