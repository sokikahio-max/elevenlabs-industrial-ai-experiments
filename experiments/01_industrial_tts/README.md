# Experiment 01 — Industrial Text-to-Speech

## Objective

Demonstrate a minimal Python integration with the ElevenLabs API for
industrial text-to-speech (TTS).

The demo converts a short industrial maintenance message into an MP3 file:

> The S7-1200 PLC reports a PROFINET communication fault.

The script also records the total API generation and file-save time.

## Architecture

```text
Industrial text message
        |
        v
Python application
        |
        v
ElevenLabs TTS API
        |
        v
Generated MP3 audio
        |
        v
Simple latency measurement
```

## Files

- `industrial_tts_demo.py` — runnable TTS demo
- `output/` — generated audio files (ignored by Git)

## Setup

From the repository root:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

Edit `.env` and add your ElevenLabs API key.

## Run

From this experiment folder:

```bash
python industrial_tts_demo.py
```

Expected console output:

```text
Audio saved to: .../output/PLC_test.mp3
Generation/save time: X.XX seconds
```

## What this experiment demonstrates

- Secure API-key loading through environment variables
- Python integration with the ElevenLabs SDK
- Use of the multilingual TTS model
- Streaming API output written to an MP3 file
- Basic latency measurement with `time.perf_counter()`
- An industrial rather than generic demonstration scenario

## Limitations

This first experiment evaluates only a single TTS request. It does not yet
measure speech quality, multilingual consistency, tool calling, end-to-end
conversational latency, or industrial task accuracy.

These are intended for later experiments in this repository.
