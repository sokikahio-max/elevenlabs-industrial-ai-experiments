import csv
import os
import time
from pathlib import Path

from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs


load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "JBFqnCBsd6RMkjVDRZzb")
MODEL_ID = os.getenv("ELEVENLABS_MODEL_ID", "eleven_multilingual_v2")

if not API_KEY:
    raise RuntimeError(
        "ELEVENLABS_API_KEY was not found. "
        "Copy .env.example to .env and add your API key."
    )

client = ElevenLabs(api_key=API_KEY)

TEST_CASES = [
    {
        "language": "English",
        "text": "The S7-1200 PLC reports a PROFINET communication fault.",
        "filename": "english_plc_fault.mp3",
    },
    {
        "language": "French",
        "text": "Le PLC S7-1200 signale un défaut de communication PROFINET.",
        "filename": "french_plc_fault.mp3",
    },
    {
        "language": "Italian",
        "text": "Il PLC S7-1200 segnala un errore di comunicazione PROFINET.",
        "filename": "italian_plc_fault.mp3",
    },
]


def generate_speech(text: str, output_file: Path) -> float:
    """Generate speech and return total generation/save time in seconds."""
    cleaned_text = text.strip()

    if not cleaned_text:
        raise ValueError("Text cannot be empty.")

    output_file.parent.mkdir(parents=True, exist_ok=True)

    start_time = time.perf_counter()

    audio = client.text_to_speech.convert(
        voice_id=VOICE_ID,
        text=cleaned_text,
        model_id=MODEL_ID,
        output_format="mp3_44100_128",
    )

    with output_file.open("wb") as audio_file:
        for chunk in audio:
            audio_file.write(chunk)

    return time.perf_counter() - start_time


def save_results(rows: list[dict], csv_file: Path) -> None:
    """Save experiment timing results to CSV."""
    csv_file.parent.mkdir(parents=True, exist_ok=True)

    with csv_file.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["language", "text", "output_file", "elapsed_seconds"],
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    output_dir = Path("output")
    results_file = Path("results") / "multilingual_tts_results.csv"

    results = []

    for case in TEST_CASES:
        output_file = output_dir / case["filename"]

        elapsed = generate_speech(
            text=case["text"],
            output_file=output_file,
        )

        results.append(
            {
                "language": case["language"],
                "text": case["text"],
                "output_file": str(output_file),
                "elapsed_seconds": f"{elapsed:.3f}",
            }
        )

        print(
            f"{case['language']}: "
            f"{elapsed:.2f} s -> {output_file}"
        )

    save_results(results, results_file)

    print(f"\nResults saved to: {results_file.resolve()}")


if __name__ == "__main__":
    main()
