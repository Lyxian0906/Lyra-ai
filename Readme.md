# Lyx AI ✨

A personal AI chat assistant built with Flask and Google's Gemini API. LyxAI remembers your conversation, has a customizable personality, and can call tools to answer questions more accurately.

## Features

- 💬 Chat interface with a constellation/starlight theme
- 🧠 Persistent memory — conversations survive server restarts
- 🎭 Customizable personality via a separate, git-ignored prompt file
- 🔧 Tool calling — Lyra can call real functions (e.g. get the current time) instead of guessing

## Setup

### 1. Fork the repo

Just click on the fork button

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your API key

Create a `.env` file in the project root (this file is git-ignored and never committed):

```
GEMINI_API_KEY=your_key_here
```

Get a key from [Google AI Studio](https://aistudio.google.com/) if you don't have one.

### 4. Set up your personality file

The real prompt (`persona.py`) is git-ignored so personal details don't end up in the public repo. Copy the placeholder to get started:

```bash
cp persona.example.py persona.py
```

Then open `persona.py` and write Lyra's actual personality, tone, and any context you want her to know about you. This file is yours — it never gets committed.

### 5. Run it

```bash
python app.py
```

Open **http://127.0.0.1:5000** in your browser. (Opening `index.html` directly as a file won't work — it has to be served by Flask.)

## File structure

```
├── app.py                 # Flask server — routes, Gemini calls, memory logic
├── persona.py              # Your real personality prompt (git-ignored, not in repo)
├── persona.example.py      # Placeholder prompt — safe to commit, copy to persona.py
├── tools.py                 # Functions Lyra can call (time lookup, project info, etc.)
├── requirements.txt        # Python dependencies
├── .env                     # Your GEMINI_API_KEY (git-ignored, not in repo)
├── .gitignore
├── conversation.json        # Auto-created on first chat — stores conversation history (git-ignored)
├── templates/
│   └── index.html          # Chat page markup
├── Script/
│   └── script.js           # Frontend chat logic (sending messages, rendering replies)
└── Styles/
    └── styles.css           # Chat UI styling
```

### What each file does

| File | Purpose |
|---|---|
| `app.py` | The Flask server. Serves the page, handles `/chat` (talks to Gemini, saves history), and `/reset` (clears history). |
| `persona.py` | Where Lyra's personality lives — tone, rules, and any context about you. Edit this to make her yours. |
| `persona.example.py` | A generic fallback so the project still runs if `persona.py` doesn't exist yet. |
| `tools.py` | Plain Python functions Lyra can call herself when they'd help answer a question. Add a function here, then list it in `app.py` to enable it. |
| `conversation.json` | The full chat history, saved automatically after every message. Delete it (or hit `/reset`) to start fresh. |

## Adding a new tool

1. Write a function in `tools.py` with type hints and a docstring — the SDK uses both to know what the function does and when to call it.
2. Import it in `app.py` and add it to the `LYRA_TOOLS` list.

That's the whole process — no manual schema writing needed.

## Learn how this works

The `docs/` folder has a set of guides for understanding this project (and
building your own version) in depth:

1. [docs/01-architecture.md](./docs/01-architecture.md) — how all the pieces fit together
2. [docs/02-backend-explained.md](./docs/02-backend-explained.md) — `app.py`, `persona.py`, `tools.py` walked through
3. [docs/03-frontend-explained.md](./docs/03-frontend-explained.md) — `index.html`, `script.js`, `styles.css` walked through
4. [docs/04-build-your-own.md](./docs/04-build-your-own.md) — a from-scratch build order, step by step
5. [docs/05-next-steps.md](./docs/05-next-steps.md) — a roadmap of what to add next, easy to hard

## Notes

- `persona.py`, `.env`, and `conversation.json` are all git-ignored on purpose — they're personal to your setup and shouldn't be shared publicly.
- If tools or persona changes don't seem to take effect, make sure you restarted `python app.py` — Flask's `debug=True` reloads on file changes, but it's worth double-checking.
