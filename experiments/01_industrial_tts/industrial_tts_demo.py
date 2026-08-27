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


def generate_speech(text: str, output_file: Path) -> float:
    """Generate speech with ElevenLabs and save it to an MP3 file."""
    if not isinstance(text, str):
        raise TypeError("Text must be a string.")

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


def main() -> None:
    text = "The S7-1200 PLC reports a PROFINET communication fault."
    output_file = Path("output") / "PLC_test.mp3"

    elapsed = generate_speech(text, output_file)

    print(f"Audio saved to: {output_file.resolve()}")
    print(f"Generation/save time: {elapsed:.2f} seconds")


if __name__ == "__main__":
    main()
