# Architecture Overview

This document outlines the high‑level architecture of the Self‑Debugging Coding Assistant.  A conceptual diagram is provided in the accompanying report.  The major components are:

## Front‑End

The front‑end provides a user interface where developers can submit prompts and view results.  It communicates with the backend over HTTPS.  The UI should display:

* A text input area for the coding prompt and optional test cases.
* A list of attempts showing the generated code, execution output and errors.
* Indicators for progress, latency and token usage.

## Backend API

The backend orchestrates the LLM calls and sandbox execution.  It exposes REST endpoints or GraphQL resolvers that the front‑end calls.  Responsibilities include:

* Receiving prompts and test cases.
* Managing sessions and iteration state.
* Invoking the LLM client to generate and refine code.
* Invoking the code executor to run code in the sandbox.
* Logging and tracing each step with Datadog.
* Returning results and attempt history to the caller.

## LLM Client

This layer wraps the Vertex AI or Gemini API.  It should abstract model selection, prompt templates, and error analysis.  It also records metrics like latency and token usage【769973766559025†L487-L518】.

## Code Execution Sandbox

Generated code is executed in an isolated sandbox environment for security.  You can use Google Cloud Functions, Cloud Run, or the Google Cloud Agent Engine Code Execution tool.  The sandbox provides process‑level isolation and persists state across iterations【756926928666265†L212-L239】【756926928666265†L274-L291】.

## Observability via Datadog

Datadog LLM Observability is used to trace prompts, responses, and intermediate steps【769973766559025†L487-L518】.  Standard RED metrics (rate, errors, duration) are monitored for the backend and the model【814637305327347†L536-L553】.  Custom metrics capture token usage per iteration, number of attempts, and sandbox resource usage.  Monitors trigger alerts when anomalies are detected.

## Self‑Healing Logic

When errors or anomalies occur (e.g., too many iterations or high token consumption), the system can adjust its behaviour automatically.  Strategies include switching to a different model, tightening the system prompt, or escalating to human review.  Datadog monitors can trigger Cloud Functions or Workflows to execute remediation actions.

Refer to the main report for a diagram illustrating these components and their interactions.