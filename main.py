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
    #"spanish": "es",
    #"french": "fr",
    #"german": "de",
    #"italian": "it",
    #"portuguese": "pt",
    #"polish": "pl",
    #"turkish": "tr",
    #"russian": "ru",
    #"dutch": "nl",
    #"czech": "cs",
    #"arabic": "ar",
    #"chinese": "zh",
    "japanese": "ja",
    #"hungarian": "hu",
    #"korean": "ko",
    #"hindi": "hi"
}

passthrough = True
while True:
    try:
        text = input("Enter text to translate: ")

        if text == "passthrough":
            print("Passthrough mode enabled.")
            passthrough = True
        elif text.lower in language_codes.keys():
            translator.load_model(language_codes[text.lower()])
            passthrough = False
        elif text.lower in language_codes.values():
            translator.load_model(text.lower())
            passthrough = False
        else:
            if passthrough:
                tts.speak(text)
            else:
                tts.speak(translator.translate(text))
                
    except KeyboardInterrupt:
        tts.stop()
        stream.stop()
        stream.close()
        break