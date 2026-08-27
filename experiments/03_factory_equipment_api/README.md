# Experiment 03 — Factory Equipment API

## Objective

Build a small deterministic factory-data service that can later be exposed as
a tool to an ElevenLabs Agent.

This experiment deliberately separates:

- **conversational intelligence** — handled later by the voice agent
- **operational truth** — returned by a deterministic backend API

That separation is useful in industrial systems because the agent should not
invent live equipment status.

## Starting Point

The original prototype exposed mock status data for `Conveyor3` and
`Conveyor7` through Flask. This phase refactors that prototype into a
GitHub-ready experiment and adds:

- a `/health` endpoint
- explicit equipment fields
- an HTTP client example
- request-latency measurement
- basic Python tests
- handling for unknown equipment IDs

## Architecture

```text
Future ElevenLabs Agent
        |
        | tool/API request
        v
Factory Equipment API
        |
        +--> Conveyor3
        |      status = high_alarm
        |      temperature = 91 C
        |
        +--> Conveyor7
               status = running
               temperature = 63 C
```

For this phase, the future agent is represented by a simple Python API client:

```text
api_client_demo.py
        |
        | HTTP GET
        v
Flask Factory API
        |
        v
JSON equipment status
```

## Endpoints

### Health check

```http
GET /health
```

Example response:

```json
{
  "status": "ok"
}
```

### Equipment status

```http
GET /equipment/Conveyor3
```

Example response:

```json
{
  "communication": "online",
  "status": "high_alarm",
  "temperature_c": 91
}
```

Unknown IDs return a controlled response rather than fabricated data:

```json
{
  "status": "unknown",
  "message": "No equipment found for ID 'UnknownConveyor'."
}
```

## Setup

Install dependencies from the repository root:

```bash
pip install -r requirements.txt
```

## Run the API

Open PowerShell in this experiment folder:

```powershell
python factory_api.py
```

The Flask API should start at:

```text
http://127.0.0.1:5000
```

Keep that terminal running.

## Run the API Client

Open a second PowerShell window in the same experiment folder:

```powershell
python api_client_demo.py
```

The client queries:

- `Conveyor3`
- `Conveyor7`
- an unknown equipment ID

and prints the JSON result plus API request latency.

## Run the Tests

From this experiment folder:

```powershell
pytest -q
```

## Why This Matters for the Voice-Agent POC

The future ElevenLabs Agent should not answer operational questions from
language-model memory.

Instead:

```text
Technician:
"What is the status of Conveyor 3?"

        |
        v

ElevenLabs Agent
        |
        | get_equipment_status("Conveyor3")
        v

Factory API
        |
        v

status = high_alarm
temperature = 91 C

        |
        v

Agent:
"Conveyor 3 is in a high-alarm state at 91 degrees Celsius."
```

The API therefore becomes the **source of truth** for live operational data.

## Current Scope

This is intentionally a mock API. It does not connect to a real PLC, SCADA,
OPC UA server, historian, or MQTT broker.

A later research extension could replace the mock dictionary with:

- OPC UA data
- MQTT telemetry
- historian queries
- ThingsBoard telemetry
- a digital twin
- a production database

without changing the basic agent-to-tool architecture.

## Next Experiment

**Experiment 04 — ElevenLabs Voice Agent with Factory Tool**

The next phase will connect an ElevenLabs Agent to this API so that a spoken
industrial question can trigger a deterministic equipment-status lookup.
