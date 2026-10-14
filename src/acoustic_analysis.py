import librosa
import numpy as np

def analyze_acoustics(filename):
    """
    Analyzes the acoustic properties of an audio file.
    """
    print(f"Analyzing acoustics for {filename}...")

    y, sr = librosa.load(filename, sr=None)

    hop_length = 512
    rms = librosa.feature.rms(y=y, hop_length=hop_length)[0]

    silence_threshold = 0.1 * np.max(rms)
    silent_frames = np.sum(rms < silence_threshold)

    frame_duration = hop_length / sr
    total_silence_duration = silent_frames * frame_duration
    total_duration = len(y) / sr

    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
    pitch_values = []

    for t in range(pitches.shape[1]):
        index = magnitudes[:, t].argmax()
        pitch = pitches[index, t]
        if pitch > 0: # Filter out noise
            pitch_values.append(pitch)


    avg_pitch = np.mean(pitch_values) if pitch_values else 0
    pitch_std = np.std(pitch_values) if pitch_values else 0
    
    print("Acoustic Analysis:")
    print(f"- Total duration: {total_duration:.2f} seconds")
    print(f"- Estimated silence: {total_silence_duration:.2f} seconds")
    print(f"- Average pitch: {avg_pitch:.1f} Hz")
    print(f"- Pitch variation (Std Dev): {pitch_std:.1f} Hz (higher = more dynamic)")
    
    return {
        "duration": total_duration,
        "silence_duration": total_silence_duration,
        "avg_pitch": avg_pitch,
        "pitch_std": pitch_std
    }

if __name__ == "__main__":
    analyze_acoustics("example_audio.wav")

