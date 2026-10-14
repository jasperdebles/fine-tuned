import sounddevice as sd 
import soundfile as sf 
import numpy as np

def record_audio(filename="sample.wav", duration=10, samplerate=16000): 
    """ 
    Record audio from the headphone and save it to a file. 
    """
    audio_data = sd.rec(
        int(duration * samplerate), 
        samplerate=samplerate, 
        channels=1, 
        dtype='float32'
    )

    sd.wait()

    print(f"Recording finished and processed")

    sf.write(filename, audio_data, samplerate) 

    print(f"Audio saved to {filename}") 

if __name__ == "__main__":
    record_audio()
