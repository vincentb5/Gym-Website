<!-- Copilot / AI agent instructions specific to the Gym-Website repo -->
# Quick Agent Guide — Gym-Website

Purpose: short, actionable guidance so an AI coding agent can be productive immediately.

**Big Picture**:
- **Framework**: Single-file Flask app in `app.py`. It currently exposes one route (`/`) and returns a plain text health message.
- **Static UI**: The user-visible site is in `static/index.html` (self-contained HTML with inline CSS). A `style.css` file exists but is empty.
- **Why this structure**: project is a very small static front-end paired with a minimal Flask server. Keep changes minimal and explicit — the codebase prefers simple, single-file edits.

**How the app runs (dev)**:
- Activate venv (PowerShell):
  ```powershell
  & .venv\Scripts\Activate.ps1
  ```
- Start the app:
  ```powershell
  python app.py
  ```
- Note: `app.py` uses `app.run(debug=True)`. Running `python app.py` is the straightforward dev flow.

**Common tasks & patterns**:
- To serve the static site from the root path (instead of the current text response), update `app.py` to return `static/index.html` using `send_from_directory`. Example:
  ```python
  from flask import Flask, send_from_directory
  app = Flask(__name__, static_folder='static')

  @app.route('/')
  def home():
      return send_from_directory('static', 'index.html')
  ```
- When changing styles, prefer moving inline CSS from `static/index.html` into `style.css` and reference it with a `<link>` tag.
- Keep server-side changes small and focused: add routes in `app.py`, mirror the existing simple style (no complex blueprints or packages).

**Project-specific conventions**:
- UI files live under `static/` and are edited directly (no Jinja templating currently). If you introduce templates, place them in a new `templates/` folder and follow Flask defaults.
- The project uses external image assets (Unsplash URL in `index.html`) — avoid embedding large binary assets into the repo.
- There are no tests or CI in the repository now. Do not add heavy test infra without discussing first.

**Integrations & dependencies**:
- Only dependency is `Flask` (implicit from `app.py`). Use the existing virtualenv `.venv` for local runs.
- External endpoints: images and contact email in `static/index.html` (no external APIs are integrated server-side).

**Safety & style notes for changes**:
- Preserve the minimal app footprint. Small, isolated edits are preferred.
- If you add new Python dependencies, update `requirements.txt` (create the file) and note why the dependency is necessary.
- Keep debug mode only for local development; do not flip `debug=True` for production changes without a clear migration plan.

**Examples of useful edits**:
- Serve the static site at `/` (example above).
- Move styles to `style.css` and update `index.html` to link it.
- Add a simple JSON API route (e.g., `/api/workouts`) that returns static sample data — keep payloads small and documented.

If anything in these instructions is unclear or you want broader scope (tests, CI, templates), ask the repo owner before implementing.

---
Please review and tell me which areas you want expanded (routing examples, styling workflow, or adding a `requirements.txt`).
