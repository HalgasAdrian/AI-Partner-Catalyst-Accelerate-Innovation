# Sequence Diagram

This document describes the typical sequence of interactions in the self‑debugging loop.  You can use a diagramming tool (e.g., Mermaid, PlantUML) to visualize this flow.  The steps are:

1. **Prompt submission** – The user submits a coding prompt and optional test cases through the front‑end.  The front‑end sends an HTTP request to the backend API.
2. **Initial code generation** – The backend invokes the `generate_code()` method on the LLM client, passing the prompt.  The LLM returns a code snippet.
3. **First execution** – The backend sends the code to the sandbox via the code executor.  The sandbox runs the code and returns standard output or an error.
4. **Evaluation** – If the code runs successfully and any provided tests pass, the backend returns the code and output to the user.  Otherwise, proceed to step 5.
5. **Error analysis** – The backend calls `analyse_errors()` on the LLM client, passing the previous code and the error message.  The LLM suggests corrections or a refined prompt.
6. **Iteration** – The backend repeats steps 3–5 using the refined code until it succeeds or reaches the maximum iteration count.  Each iteration is traced and metrics are recorded.
7. **Self‑healing** – If the maximum iterations is reached, the backend may trigger a fallback strategy (e.g., switch models, adjust prompts, or create an incident)【756926928666265†L212-L239】.
8. **Response** – The backend returns the final result (code, output, attempt history) to the front‑end, which displays it to the user.

By following this sequence, the assistant behaves like a developer who writes, tests and refines code until it works.