# AI-Driven Pitch & Interview Analyzer

An end-to-end Python pipeline that captures real-time voice input, extracts acoustic metrics (pitch, cadence, silence detection), transcribes speech using OpenAI Whisper, and generates a structured, professional feedback report using Google Gemini AI.

---

## System Architecture

The application is structured into four distinct modular stages, ensuring a clean separation of concerns from hardware ingestion to AI evaluation:

```mermaid
graph TD
    subgraph Input ["1. Audio Ingestion"]
        Mic["Microphone Input"] --> Buffer["Audio Stream / Buffer"]
    end

    subgraph Processing ["2. Signal Processing & STT"]
        Buffer --> Pitch["Pitch Extraction (F0)"]
        Buffer --> Cadence["Cadence & WPM"]
        Buffer --> VAD["Voice Activity & Pauses"]
        Buffer --> STT["Speech-to-Text (Whisper)"]
    end

    subgraph Intelligence ["3. Multi-Modal Analysis & Evaluation"]
        Pitch & Cadence & VAD --> Metrics["Acoustic Metrics Aggregator"]
        STT --> Transcript["Text Transcript & Keywords"]
        Metrics & Transcript --> LLM["Google Gemini AI Coach"]
    end

    subgraph Output ["4. Output"]
        LLM --> Report["Structured Feedback Report"]
    end

    style Input fill:#1f2328,stroke:#388bfd,stroke-width:2px,color:#fff
    style Processing fill:#1f2328,stroke:#238636,stroke-width:2px,color:#fff
    style Intelligence fill:#1f2328,stroke:#8957e5,stroke-width:2px,color:#fff
    style Output fill:#1f2328,stroke:#da3633,stroke-width:2px,color:#fff