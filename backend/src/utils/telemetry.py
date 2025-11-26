"""Utility functions for observability.

This module should encapsulate the logic for sending traces, metrics and logs to
Datadog.  You can use Datadog’s Python libraries (e.g. `ddtrace` for tracing
and `datadog` or `dogstatsd` for metrics).  Key points to capture include:

* Prompt and response traces from the LLM client, including latency, token
  usage and model name【769973766559025†L487-L518】.
* Execution metrics such as run duration, memory usage and CPU usage
  (available from the sandbox environment)【814637305327347†L536-L553】.
* Custom metrics for the number of iterations, number of test cases passed,
  token counts per attempt, etc.

You should also provide helper functions to wrap code blocks in trace spans and
send logs with contextual metadata.  See the Datadog documentation for
examples.

Note: The actual implementation is not provided here; implement these
functions when integrating with Datadog.
"""

def start_trace(name: str):
    """Start a new trace span.

    Replace this stub with a context manager or decorator that initiates a trace
    with Datadog’s tracing library.
    """
    raise NotImplementedError


def record_metric(name: str, value: float, tags: list[str] | None = None):
    """Record a custom metric.

    Use Datadog’s StatsD client to send gauge or counter metrics.  Include
    optional tags (e.g. iteration number, model name) for filtering on the
    Datadog dashboard.
    """
    raise NotImplementedError


def log_event(title: str, text: str, alert_type: str = "info"):
    """Send an event to Datadog.

    Events can be attached to monitors or incidents.  Use this to record
    significant occurrences like a fallback to a secondary model or the end of
    the self‑debugging loop.
    """
    raise NotImplementedError