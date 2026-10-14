import os 
from google import genai

from settings import AI_MODEL

def evaluate_pitch(transcript_text: str, metrics: dict) -> str: 
    """
    Evaluates the pitch based on the combination of the transcript text and acoustic metrics provided.
    Returns a string containing constructive feedback.
    """

    client = genai.Client()

    prompt = f"""
    You are an expert in evaluating pitches and job interview presentations. 
    Below is the transcript of the recorded audio data and the associated acoustic metrics:

    Transcript: {transcript_text}
    Acoustic Metrics: {metrics}

    Evaluate the pitch based on the transcript and acoustic metrics.
    
    Content & Verbal Communication
    (Analyze the structure, wording, and clarity of the transcript)

    Pacing, Pauses & Time Utilization
    (Analyze the pacing, strategic use of pauses, and overall time management based on the metrics)
    
    Vocal Acoustics & Delivery
    (Analyze the pace, pauses/silence, and pitch variation based on the metrics)
    
    Actionable Recommendations
    (Provide specific, actionable suggestions for improvement)
    """

    response = client.models.generate_content(
        model = AI_MODEL,
        contents = prompt
    )

    return response.text