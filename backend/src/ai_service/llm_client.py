"""LLM Client wrapper.

This module encapsulates all interactions with the Vertex AI (or Gemini) API for
code generation and error analysis.  It should handle authentication using
service accounts, manage prompt templates, and provide helper functions such as:

* `generate_code(prompt: str) -> str`: Generate initial code from a user prompt.
* `analyse_errors(code: str, error_message: str) -> str`: Given code and an error
  message, ask the model to suggest corrections or refined prompts.
* `select_model(iteration: int) -> str`: Optionally choose a different model or
  prompt strategy based on how many iterations have been attempted.

The client should record timing, token counts and other metrics as custom spans
and send them to Datadog (see `utils/telemetry.py`).  Avoid embedding secrets
directly in the code; read them from environment variables or your configuration
management system.

No actual API calls are provided here; fill in the implementation when ready.
"""

class LLMClient:
    """A simple interface for interacting with the LLM."""

    def __init__(self, model_name: str, project: str, region: str):
        self.model_name = model_name
        self.project = project
        self.region = region

    def generate_code(self, prompt: str) -> str:
        """Generate code based on a textual prompt.

        Replace this stub with code that calls the Vertex AI API and returns the
        generated code.  Remember to capture relevant metrics (latency, token
        usage) for observability.
        """
        raise NotImplementedError

    def analyse_errors(self, code: str, error_message: str) -> str:
        """Ask the model to correct the code or refine the prompt after a failure.

        Replace this stub with code that sends the failing code and error
        message to the LLM and returns a corrected code snippet or a refined
        instruction.  Capture metrics as needed.
        """
        raise NotImplementedError

    def select_model(self, iteration: int) -> str:
        """Optionally select a different model depending on the iteration count.

        For example, after several failed attempts you might fall back to a
        smaller, more deterministic model or adjust the system prompt.  This
        method should return the name of the model to use.
        """
        return self.model_name