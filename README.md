# ElevenLabs Industrial AI Experiments

Small proof-of-concept experiments exploring voice AI and conversational AI
for industrial and smart-manufacturing environments.

## Motivation

Industrial users often need fast access to operational information while
working with machines, alarms, maintenance procedures, and production
systems. Voice interfaces can provide a natural interaction layer over
existing industrial data and services.

This repository develops the idea incrementally, beginning with basic
industrial text-to-speech and later extending toward multilingual voice
interaction, tool/API integration, equipment-status retrieval, and measured
agent performance.

## Experiment Roadmap

| Experiment | Focus | Status |
|---|---|---|
| 01 | Industrial text-to-speech with ElevenLabs | Available |
| 02 | Multilingual industrial TTS | Available |
| 03 | Factory equipment API tool | Planned |
| 04 | Voice agent with industrial tools | Planned |
| 05 | Latency and performance evaluation | Planned |

## Available Experiments

### 01 — Industrial Text-to-Speech

A Python script sends an industrial maintenance message to the ElevenLabs
TTS API, saves the generated audio as MP3, and records generation/save time.

`experiments/01_industrial_tts/README.md`

### 02 — Multilingual Industrial Text-to-Speech

Runs semantically equivalent industrial fault messages in English, French,
and Italian using the same multilingual ElevenLabs TTS configuration and
stores timing results for comparison.

`experiments/02_multilingual_tts/README.md`

## Repository Structure

```text
elevenlabs-industrial-ai-experiments/
|
|-- README.md
|-- requirements.txt
|-- .env.example
|-- .gitignore
|-- LICENSE
|
`-- experiments/
    |-- 01_industrial_tts/
    |   |-- README.md
    |   |-- industrial_tts_demo.py
    |   `-- output/
    |
    `-- 02_multilingual_tts/
        |-- README.md
        |-- multilingual_tts_demo.py
        |-- output/
        `-- results/
```

## Quick Start

```bash
python -m venv .venv
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and add your ElevenLabs API key.

Then:

```bash
cd experiments/01_industrial_tts
python industrial_tts_demo.py
```

## Security

Never commit API keys, `.env` files, access tokens, or private customer data.
This repository intentionally loads credentials from environment variables.

## Future Direction

Planned extensions include:

- multilingual industrial voice interaction
- real-time equipment-status lookup through Python APIs
- ElevenLabs Agent tool integration
- deterministic grounding of operational facts
- latency, correctness, and multilingual evaluation
- reproducible experiment datasets suitable for later research analysis

## Disclaimer

This repository contains independent proof-of-concept experiments built
with publicly available ElevenLabs APIs/SDKs. It is not an official
ElevenLabs repository or product.
