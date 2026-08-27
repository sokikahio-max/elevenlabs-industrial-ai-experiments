# Experiment 02 — Multilingual Industrial Text-to-Speech

## Objective

Evaluate a simple multilingual industrial TTS workflow using the same
ElevenLabs model and voice configuration across English, French, and Italian.

The experiment uses semantically equivalent industrial fault messages in all
three languages and records the generation/save time for each request.

## Research Question

> Can the same multilingual TTS setup produce usable industrial voice output
> across multiple languages while preserving technical terminology such as
> PLC, S7-1200, and PROFINET?

## Test Messages

### English

> The S7-1200 PLC reports a PROFINET communication fault.

### French

> Le PLC S7-1200 signale un défaut de communication PROFINET.

### Italian

> Il PLC S7-1200 segnala un errore di comunicazione PROFINET.

## Architecture

```text
English text  ----\
French text   -----+--> Python --> ElevenLabs multilingual TTS --> MP3
Italian text  ----/                         |
                                             v
                                  latency measurement
                                             |
                                             v
                                      results CSV
```

## Files

- `multilingual_tts_demo.py` — runs the three language tests
- `output/` — generated MP3 files
- `results/multilingual_tts_results.csv` — timing results created at runtime

Generated audio and runtime CSV results are ignored by Git by default.

## Run

From this experiment folder:

```bash
python multilingual_tts_demo.py
```

Expected console output:

```text
English: X.XX s -> output/english_plc_fault.mp3
French: X.XX s -> output/french_plc_fault.mp3
Italian: X.XX s -> output/italian_plc_fault.mp3

Results saved to: .../results/multilingual_tts_results.csv
```

## Measurements

The current experiment records:

- language
- input text
- generated audio filename
- total generation/save time

## Manual Evaluation

After generating the audio, listen to each file and record qualitative notes
for:

- intelligibility
- pronunciation of `S7-1200`
- pronunciation of `PLC`
- pronunciation of `PROFINET`
- naturalness
- consistency across languages

A later phase can turn these observations into a structured evaluation table.

## Limitations

This experiment does not yet measure:

- speech-quality scores
- pronunciation accuracy automatically
- end-to-end conversational latency
- speech-to-text performance
- tool/API calling
- industrial task correctness

These are intentionally left for later experiments.
