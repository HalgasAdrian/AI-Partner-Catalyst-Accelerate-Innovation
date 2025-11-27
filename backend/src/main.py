from typing import Union
from fastapi import FastAPI

"""Entry point for the backend API server.

This module defines the HTTP API that the front‑end will interact with.  Use a framework like
FastAPI or Flask to expose endpoints for:

* Submitting a coding prompt and optional test cases.
* Returning the generated code, test results, and any error messages.
* Exposing health or metrics endpoints for monitoring.

The implementation should orchestrate calls to the LLM client (for code generation and
analysis) and the code execution sandbox.  It should also integrate Datadog for tracing
and metrics.  See `ai_service/app.py` for the core logic.

Note: this file intentionally contains no executable code; you will need to fill it in
during implementation.
"""

app = FastAPI()

@app.post("/generate")
def generate_code(prompt: str, tests: Union[list[str], None] = None):
    """Endpoint to generate and self-debug code based on a user prompt.

    Arguments:
        prompt:  The natural language description of the desired code.
        tests:   Optional list of test case definitions that validate the code."""

@app.get("/result/{session_id}")
def get_result(session_id: str):
    """Endpoint to retrieve the result of a self-debugging session.

    Arguments:
        session_id:  The unique identifier for the coding session."""

@app.get("/healthz")
def health_check():
    """Health check endpoint to verify the service is running."""
    return {"status": "ok"}
