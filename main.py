from xtts_live.xtts_live import TextToSpeech
import sounddevice as sd


tts = TextToSpeech()

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = tts.audio_buffer.get_samples(frames)








def main():
    stream = sd.Stream(callback=callback)
    stream.start()
    tts.speak("Hello World")
    stream.stop()