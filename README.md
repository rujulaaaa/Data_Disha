# MagicBus — AI Analytics Agent
Project submission for the AI Analytics Hackathon (IIT Bombay Research Park)

A FastAPI-based backend that ingests CSVs, runs analytics using a local LLM-based agent, and exposes endpoints for upload, ingestion and natural-language querying of analytics results.

## Repository overview
- backend/app/main.py — FastAPI application and router registration
- backend/app/routers/ — API route modules:
  - upload.py — file upload endpoints
  - ingest.py (or routers/ingest.py) — CSV ingestion into storage/processing
  - query.py — natural-language query endpoint that calls analytics agent
  - reports.py — report generation endpoints
  - health.py — health-check endpoint
  - auth.py — authentication-related routes (if present)
- backend/app/core/ — core runtime components:
  - llm_engine.py — LocalLLMEngine wrapping a Hugging Face causal LLM (mistralai/Mistral-7B-Instruct-v0.2 by default)
  - agent.py — analytics agent logic that interprets queries and runs pipelines (invoked by query router)
- backend/app/models/ — Pydantic request/response models (e.g., QueryRequest)
- backend/app/storage/uploads/ — default upload directory (CSV files)
- other project files: requirements.txt (if present), scripts, config

## Key technologies
- FastAPI + Uvicorn (ASGI server)
- Transformers (Hugging Face) + PyTorch for local LLM inference
- anyio / concurrency primitives if needed for blocking work
- CSV parsing / pandas (optional in ingestion pipeline)
- oneDNN/tensor optimizations shown in runtime logs

## Quick start (development)
1. Clone repository and cd into project root:
   cd /home/rujula/data_disha

2. Create and activate virtual environment (recommended):
   python3 -m venv .venv
   source .venv/bin/activate

3. Install dependencies. If repo contains requirements.txt:
   pip install -r requirements.txt
   Otherwise install typical stack:
   pip install fastapi uvicorn "transformers[sentencepiece]" torch

   Notes:
   - For local inference of large models (Mistral-7B-Instruct) you need a GPU and sufficient VRAM.
   - To reduce memory, model is loaded with torch_dtype=float16 and device_map="auto" in llm_engine.py.

4. Start the server (from repo root):
   uvicorn backend.app.main:app --reload --port 8000

5. Open interactive docs:
   http://127.0.0.1:8000/docs

## Example API usage
- Upload a file (if upload endpoint expects multipart):
  curl -v -X POST "http://127.0.0.1:8000/api/upload/" -F "file=@/path/to/Book1.csv"

- Ingest an uploaded CSV (example used in repo):
  curl -v -X POST "http://127.0.0.1:8000/api/ingest/?filename=Book1.csv"

- Query (natural language):
  curl -v -X POST "http://127.0.0.1:8000/api/query/" -H "Content-Type: application/json" -d '{"query":"sum of Donations (INR)"}'

If routes are registered without the `/api` prefix for some routers, confirm the registered route list via:
python - <<'PY'
from backend.app.main import app
print([{"path":r.path,"methods":list(r.methods)} for r in app.routes])
PY

## Operational notes & troubleshooting
- Large-model inference:
  - The default model is `mistralai/Mistral-7B-Instruct-v0.2`. Downloading/loading may be slow and memory intensive.
  - If you do not have a capable GPU, change model loading in backend/app/core/llm_engine.py to use a smaller model or set `device_map="cpu"` and lower `torch_dtype`.
  - Set environment variable to reduce transformer verbosity: `export TRANSFORMERS_VERBOSITY=info`

- 500 errors from /api/query/:
  - Ensure analytics_agent.run is called correctly. If it is blocking or CPU/GPU heavy, run it in a thread (e.g., anyio.to_thread.run_sync) from an async endpoint.
  - Add logging or a temporary exception handler in main.py to capture full traceback while debugging.

- Route prefix consistency:
  - Some routers are included with `prefix="/api"` and others without. For predictable API paths, include all routers with the same prefix (edit backend/app/main.py).

- File-not-found on ingest:
  - Ensure you either upload the file first to storage/uploads or send the file in the ingestion request depending on the ingest handler implementation.
  - Default upload storage: backend/app/storage/uploads/

## Configuration & customization
- Change the LLM model by editing `model_id` in backend/app/core/llm_engine.py.
- Tune generation (temperature, max_new_tokens) in LocalLLMEngine.generate.
- If using Hugging Face private models or tokens, set HF_TOKEN env var and pass it to from_pretrained calls.

## Development tips
- Use `--log-level debug` with uvicorn to see full tracebacks:
  uvicorn backend.app.main:app --reload --port 8000 --log-level debug

- For long-running or blocking agent tasks, prefer running in a background thread or a task queue (RQ/Celery) to keep FastAPI responsive.

## Submission note
This repository is submitted as the project entry for the AI Analytics Hackathon organized under IIT Bombay Research Park. It demonstrates an end-to-end prototype for CSV ingestion, LLM-driven analytics and queryable results.

## Contact
For internal project details and reproducibility, inspect the code in backend/app and follow the Quick start steps above.
