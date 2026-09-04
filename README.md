# F1 Live Telemetry & Driver Persistence Pipeline 🏎️

A modular, decoupled backend system engineered in Python to ingest real-time Formula 1 session telemetry via the OpenF1 API, validate and encapsulate entity schemas, persist state into PostgreSQL with conflict handling, and serve optimized REST endpoints via FastAPI.

---

## Architectural Design

The project is structured into three decoupled layers:

```text
[ External OpenF1 API ]
          │
          ▼
   ( services/api.py ) ──────► Live HTTP Ingestion Client
          │
          ▼
   ( core/models.py )  ──────► Domain Encapsulation & Tuple Adapters
          │
          ▼
  ( core/database.py ) ──────► PostgreSQL Persistence (Idempotent ON CONFLICT)
          │
          ├───────────────────────────────┐
          ▼                               ▼
 [ pipeline.py (ETL Ingestion) ]   [ app.py (FastAPI REST Server) ]
                                          │
                                          ▼
                               [ Client / Swagger Docs ]
```
Layer 1: Domain Modeling & Encapsulation (models.py)
Defensive Ingestion: Safely unpacks dynamic dictionary payloads extracted from upstream telemetry feeds.

Decoupling Adapter: Uses to_tuple() serialization to decouple domain entities from database persistence layers.

Layer 2: Persistence & Idempotency (database.py, pipeline.py)
Relational Storage: PostgreSQL integration via psycopg2 with environment-driven credentials (.env).

Idempotent Ingestion: Employs SQL ON CONFLICT (driver_number) DO NOTHING clauses to prevent duplicate writes during repetitive telemetry runs.

Layer 3: REST API Delivery (app.py)
Asynchronous Service: Exposes structured endpoints for driver directory queries and single-record retrieval.

Auto-Documentation: Built-in OpenAPI specification available at /docs.

## Repository Structure

```text
├── app.py              # FastAPI application server & REST endpoints
├── pipeline.py         # Standalone ingestion runner (Fetch -> Model -> Persist)
├── api.py              # OpenF1 live API integration client
├── database.py         # PostgreSQL DatabaseManager & schema initialization
├── models.py           # Core domain entity (Driver) and adapter methods
├── test_models.py      # Unit-level model integrity tests
├── Dockerfile          # Containerized runtime definition
├── requirements.txt    # Production dependency pins
└── .gitignore          # Environment & secret shielding
```

---

## Setup & Execution

### 1. Environment Configuration
Create a `.env` file in the root directory:
```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=f1_db
DB_USER=your_user
DB_PASSWORD=your_password
```

### 2. Install Dependencies
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Run Verification Tests
```bash
python3 test_models.py
```

### 4. Execute the Ingestion Pipeline
```bash
python3 pipeline.py
```

### 5. Launch the REST API Server
```bash
uvicorn app:app --reload --port 8000
```
Interactive docs will be available at `http://localhost:8000/docs`.

