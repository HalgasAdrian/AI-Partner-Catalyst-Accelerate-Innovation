# Self‑Debugging Coding Assistant

This repository contains a scaffold for the **Self‑Debugging Coding Assistant** hackathon project.  The goal of the project is to build a cloud‑native application that uses a Large Language Model (LLM) to generate code from a user’s prompt, execute it in a safe sandbox, analyse any errors, and refine the code until it passes tests.  The backend is instrumented with Datadog LLM Observability so you can trace each step (generation, execution, evaluation) and set up alerts or automated remediation when things go wrong.

This scaffold is intentionally light on implementation details.  It provides the file structure, configuration placeholders and commentary so you can fill in the logic as you build the project.  Follow the guide in the `/docs` folder and the accompanying report for step‑by‑step instructions on how to implement each component.

## Project structure

```
self_debug_project/
├── backend/                  # Backend service using Python and FastAPI (suggested)
│   ├── src/
│   │   ├── main.py           # Entry point for the API server
│   │   ├── ai_service/
│   │   │   ├── llm_client.py # Wrapper around the Vertex AI API for code generation and analysis
│   │   │   ├── executor.py   # Logic for sending code to the sandbox and retrieving results
│   │   │   └── app.py        # Application logic orchestrating the generate→test→refine loop
│   │   └── utils/
│   │       └── telemetry.py  # Helper functions for sending metrics and traces to Datadog
│   ├── tests/                # Place your unit tests here
│   └── requirements.txt      # Python dependencies
├── frontend/                 # Minimal front‑end (React or any framework of your choice)
│   ├── src/
│   │   ├── index.html        # HTML page mounting the application
│   │   └── App.jsx           # Root component; implement the chat UI here
│   └── package.json          # Front‑end dependencies and scripts
├── infrastructure/           # Infrastructure as code templates (Terraform suggested)
│   ├── terraform/
│   │   ├── main.tf           # Resources for Cloud Run/Functions, service accounts, etc.
│   │   ├── variables.tf      # Input variables
│   │   └── outputs.tf        # Output values
│   └── datadog/
│       ├── monitors.yaml     # Declarative definitions for Datadog monitors (alerts)
│       └── dashboard.json    # JSON export of the custom Datadog dashboard
├── docs/
│   ├── architecture.md       # High‑level architecture description and diagrams
│   └── sequence_diagram.md   # Sequence or flow diagrams explaining the logic
├── .env.example              # Example environment variables (rename to .env when used)
└── .gitignore                # Standard ignore patterns for Python/Node projects
```

## Getting started

1. **Install prerequisites**: You will need Python 3.10+, Node.js (if you choose React), Terraform (optional), and the Google Cloud and Datadog command‑line interfaces.  Refer to the documentation for installation steps.
2. **Create your `.env` file**: Copy `.env.example` to `.env` and set your API keys, service account names, project IDs and other secrets.  Never commit sensitive data.
3. **Install backend dependencies**: Navigate to `backend/` and run `pip install -r requirements.txt`.  For local development you can use `uvicorn` to serve the API.
4. **Install frontend dependencies**: Navigate to `frontend/` and run `npm install`.  Use your favourite package manager (npm, pnpm, or yarn).  To run the dev server use `npm run start`.
5. **Terraform**: Modify the variables in `infrastructure/terraform/variables.tf`, then run `terraform init`, `terraform plan` and `terraform apply` to provision your Google Cloud resources.
6. **Datadog**: Use the files in `infrastructure/datadog/` to create monitors and dashboards.  You can import the JSON directly in Datadog’s UI.

For more details on each step, consult the documentation in the `/docs` folder and the accompanying report.