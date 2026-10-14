from src.audio_ingestion import record_audio
from src.speech_to_text import transcribe_audio
from src.acoustic_analysis import analyze_acoustics
from src.ai_evaluator import evaluate_pitch

def main():
    print(f"Starting Pitch & Interview Analyzer Pipeline...")
    
    audio_file = "pitch_sample.wav"
    
    record_audio(filename=audio_file, duration=10)
    
    print("\n----------------------------------------")
    transcript_text = transcribe_audio(filename=audio_file)
    
    print("\n----------------------------------------")
    metrics = analyze_acoustics(filename=audio_file)
    
    print("\nAI Agent analyzing your pitch...")
    feedback_report = evaluate_pitch(transcript_text, metrics)
    
    print("="*50)
    print("YOUR AI PITCH COACH REPORT")
    print("="*50)
    print(feedback_report)
    print("="*50)

if __name__ == "__main__":
    main()