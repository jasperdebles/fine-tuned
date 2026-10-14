import whisper 
from settings import LANGUAGE

def transcribe_audio(filename, language=LANGUAGE):
    """
    Uses the whisper model to transcribe audio from a .wav file to text. 
    """

    if filename == "" or filename == None: 
        raise ValueError("Filename must be provided")

    print(f"Loading whisper model...")

    model = whisper.load_model("base")

    print(f"Transcribing audio from {filename}...")

    result = model.transcribe(filename, language=language)
    transcript_text = result["text"]
    if not isinstance(transcript_text, str):
        raise TypeError("Whisper returned a non-string transcript")

    print(f"Transcription finished:")
    print("=" * 40)
    print(transcript_text)
    print("=" * 40)

    return transcript_text

if __name__ == "__main__":
    transcribe_audio("example.wav")