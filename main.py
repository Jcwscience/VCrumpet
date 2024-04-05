from translator import Translator
from xtts_live.xtts_live import TextToSpeech
import sounddevice as sd


# Initialize the Translator and TextToSpeechSystem
translator = Translator()

model_path = "/home/john/Documents/XTTS-v2/"  # Path to the model directory
speaker_wavs = "/home/john/Documents/Voices/voice.wav"  # Path to the speaker's audio file
output_samplerate = 48000  # Output audio sample rate

tts = TextToSpeech(model_path, speaker_wavs, output_samplerate, use_deepspeed=True, debug=False)
supported_languages = tts.supported_languages

def stream_callback(outdata, frames, time, status):
    outdata[:] = tts.audio_buffer.get_samples(frames)

stream = sd.OutputStream(
    device=20,  # Specify the audio output device index
    samplerate=output_samplerate,
    channels=1,
    callback=stream_callback,
    dtype='float32'
)

stream.start()  

while True:
    try:
        text = input("Enter text to translate: ")
        target_lang = input("Enter target language: ")
        if target_lang in supported_languages:
            print(translator.translate(text, target_lang))
            tts.speak(translator.translate(text, target_lang), target_lang)
        else:
            print(f"Language {target_lang} not supported.")

    except KeyboardInterrupt:
        tts.stop()
        stream.stop()
        stream.close()
        break