from flask import Flask, jsonify


app = Flask(__name__)


EQUIPMENT = {
    "Conveyor3": {
        "status": "high_alarm",
        "temperature_c": 91,
        "communication": "online",
    },
    "Conveyor7": {
        "status": "running",
        "temperature_c": 63,
        "communication": "online",
    },
}


def get_equipment_status(equipment_id: str) -> dict:
    """Return mock factory equipment status for a known equipment ID."""
    return EQUIPMENT.get(
        equipment_id,
        {
            "status": "unknown",
            "message": f"No equipment found for ID '{equipment_id}'.",
        },
    )


@app.get("/health")
def health():
    """Simple health endpoint for local testing."""
    return jsonify({"status": "ok"})


@app.get("/equipment/<equipment_id>")
def equipment_status(equipment_id: str):
    """Expose equipment status through HTTP."""
    return jsonify(get_equipment_status(equipment_id))


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True,
    )
