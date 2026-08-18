# What Else You Can Add

Roughly ordered from easiest to hardest. Pick based on what would actually
make you use Lyra more, not just what's technically impressive.

## Easy — an afternoon each

- **Wire up the `/reset` button** — backend already supports it; just needs
  a button in `index.html` calling it (see the earlier chat for the exact
  snippet).
- **More tools in `tools.py`** — a word/character counter, a dice roller, a
  unit converter, a joke generator. Good practice for the tool-writing
  pattern before attempting harder ones.
- **Markdown rendering for replies** — right now Lyra's text is inserted as
  plain text. If she ever replies with a code block or a list, it'll look
  flat. A small library like `marked.js` can render it properly in the
  browser.
- **Timestamps on messages** — small UI addition, teaches you how to pass
  more structured data than just `{response: "..."}` between backend and
  frontend.

## Medium — a weekend project each

- **Cap conversation history** — right now `conversation.json` grows
  forever and gets fully resent every message. Once it's long, that's slow
  and burns tokens. Cap `load_history()` to the last ~20 turns, or
  summarize older turns into a shorter blurb.
- **Multiple conversations** — right now there's exactly one conversation
  ever. Adding a `conversation_id` and storing history per-ID (e.g. one
  JSON file per conversation, or a SQLite table) lets you have separate
  threads — one for coding help, one for casual chat, etc.
- **Streaming responses** — right now you wait for the full reply before
  seeing anything. Gemini supports streaming, where text appears word by
  word like ChatGPT. This touches both `app.py` (streaming endpoint) and
  `script.js` (reading a stream instead of one JSON blob).
- **Voice input/output** — Web Speech API on the frontend for voice-to-text
  input, and a text-to-speech call for Lyra's replies.

## Harder — real projects

- **RAG (retrieval-augmented generation)** — instead of hardcoding your
  project info in `persona.py`, store notes/docs about your actual projects
  somewhere searchable (even a folder of `.md` files), and pull the
  relevant snippet into the prompt before each call. This is how you'd
  scale from "a few facts in the system prompt" to "Lyra actually knows
  everything about your codebase."
- **Real tool integrations** — instead of toy functions, connect tools to
  real things: read your GitHub issues, check your calendar, search your
  notes app. Same function-calling pattern as `tools.py`, just backed by
  real APIs instead of hardcoded dictionaries.
- **A proper database instead of JSON files** — SQLite is a natural next
  step once you have multiple conversations or want to query history
  ("what did I ask Lyra about FloopyChicken last week?").
- **Deploy it somewhere** — right now it only runs on your machine. Hosting
  it (Render, Railway, Fly.io, etc.) means using it from your phone, not
  just `127.0.0.1`. This also means finally caring about things like rate
  limiting and not exposing `debug=True` in production.

## A sensible order if you want one

1. Reset button (finish what's started)
2. A couple more tools
3. Cap the history / add basic summarization
4. Multiple conversations
5. Everything else, in whatever order excites you most

There's no wrong order beyond that — build whatever you'll actually keep
using.
