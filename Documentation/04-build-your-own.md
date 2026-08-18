# Build One Yourself, From Scratch

This walks through the same project as a from-zero build order, so you
understand *why* each piece exists, not just what it does. Do these in
order — each step only makes sense once the previous one works.

## Step 1 — Prove the API works, no web layer at all

Before any Flask, any HTML, anything — get a plain Python script talking to
Gemini in the terminal. This is exactly what your original `app.py` was
before we touched it:

```python
from google import genai
client = genai.Client(api_key="your-key")
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="hello"
)
print(response.text)
```

Get this working first. If this doesn't work, nothing built on top of it
will either — debug at this level, not in the browser.

## Step 2 — Wrap it in a web server

Swap `input()`/`print()` for a Flask route that does the same thing, but
returns JSON instead of printing:

```python
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    message = request.get_json()["message"]
    response = client.models.generate_content(model="gemini-3.6-flash", contents=message)
    return jsonify({"response": response.text})

app.run(debug=True)
```

Test it with `curl` before building any frontend:
```bash
curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d '{"message":"hello"}'
```
If you get a JSON reply back, your server layer works. Now you know any
frontend bugs later are frontend bugs, not backend ones.

## Step 3 — Add a bare-minimum frontend

One HTML file, one `fetch()` call, no styling. Just prove the browser can
hit `/chat` and display the result. Resist the urge to make it pretty yet —
you want the *smallest* number of moving parts while you're still debugging
the connection.

## Step 4 — Add memory

Without this, every message is amnesia — the model has no idea what you
said one message ago. Add a list that grows with every turn, and pass the
whole list as `contents` instead of just the latest string. Persist it to a
JSON file so it survives restarts (see `02-backend-explained.md` for the
exact pattern).

## Step 5 — Give it an identity

Add a `system_instruction` — this is the single highest-leverage change for
making an assistant feel like "yours." Write it as if you're briefing a new
employee: who they are, how they should talk, what they know about you.

## Step 6 — Add tools

Only once the above feels solid. Start with one trivial tool (current time
is a good first one — easy to verify it worked). Confirm the model actually
calls it before adding anything more ambitious.

## Step 7 — Make it pretty

Styling last, on purpose. It's tempting to do this first because it's the
most visually satisfying, but a pretty UI on top of a broken backend just
hides where the bug is.

## The general lesson

This order — **raw API call → server → dumb frontend → memory → identity →
tools → polish** — generalizes to basically any AI app you'll build later.
Each layer should fully work in isolation before you add the next one on
top of it.

Next: [05-next-steps.md](./05-next-steps.md)
