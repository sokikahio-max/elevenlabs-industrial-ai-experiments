import json
import time

import requests


BASE_URL = "http://127.0.0.1:5000"


def fetch_equipment_status(equipment_id: str) -> tuple[dict, float]:
    """Fetch one equipment record and return data plus request latency."""
    start = time.perf_counter()

    response = requests.get(
        f"{BASE_URL}/equipment/{equipment_id}",
        timeout=5,
    )
    response.raise_for_status()

    elapsed = time.perf_counter() - start
    return response.json(), elapsed


def main() -> None:
    for equipment_id in ("Conveyor3", "Conveyor7", "UnknownConveyor"):
        data, elapsed = fetch_equipment_status(equipment_id)

        print(f"\nEquipment: {equipment_id}")
        print(json.dumps(data, indent=2))
        print(f"API latency: {elapsed:.3f} seconds")


if __name__ == "__main__":
    main()
