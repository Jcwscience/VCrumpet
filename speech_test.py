import sounddevice as sd
import whisperx
import numpy as np

model = whisperx.load_model("small.en", "cuda", compute_type="int8")

class AudioBuffer:
    def __init__(self):
        self.buffer = np.array([], dtype=np.float32)

    def add_data(self, new_data):
        self.buffer = np.concatenate((self.buffer, new_data), axis=0)

    def get_samples(self):
        return self.buffer
    
buffer = AudioBuffer()

def callback(indata, outdata, frames, time, status):
    print(len(indata))


stream = sd.Stream(samplerate=48000, channels=1, blocksize=48000, dtype='float32', device=19, callback=callback)


while True:
    input("Press Enter to record")
    stream.start()
    input("Press Enter to transcribe")
    stream.stop()
    data = buffer.get_samples()
    result = model.transcribe(data, batch_size=1)
    print(result)
