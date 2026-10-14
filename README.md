"""
graph TD
    subgraph Input ["1. Audio Ingestion"]
        Mic["Microphone Input"] --> Buffer["Audio Stream / Buffer"]
    end

    subgraph Processing ["2. Signal Processing & STT"]
        Buffer --> Pitch["Pitch Extraction (F0)"]
        Buffer --> Cadence["Cadence & WPM"]
        Buffer --> VAD["Voice Activity & Pauses"]
        Buffer --> STT["Speech-to-Text (e.g. Whisper)"]
    end

    subgraph Intelligence ["3. Multi-Modal Analysis & Evaluation"]
        Pitch & Cadence & VAD --> Metrics["Acoustic Metrics Aggregator"]
        STT --> Transcript["Text Transcript & Keywords"]
        Metrics & Transcript --> LLM["AI Agents / Evaluation Engine"]
    end

    subgraph Output ["4. Output"]
        LLM --> Report["Structured Feedback Report"]
    end

    style Input fill:#1f2328,stroke:#388bfd,stroke-width:2px,color:#fff
    style Processing fill:#1f2328,stroke:#238636,stroke-width:2px,color:#fff
    style Intelligence fill:#1f2328,stroke:#8957e5,stroke-width:2px,color:#fff
    style Output fill:#1f2328,stroke:#da3633,stroke-width:2px,color:#fff