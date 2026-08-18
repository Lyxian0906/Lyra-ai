# The Frontend, Piece by Piece

The frontend's whole job is: show messages, send messages, never touch
Gemini directly. All the "thinking" happens on the server.

## `templates/index.html`

The static skeleton: a header with Lyra's name, an empty `<div id="messages">`
that JavaScript fills in at runtime, and an input + send button at the
bottom. Nothing here changes while the app runs — `script.js` mutates the
DOM inside `#messages`, it never edits this file.

Why `templates/`? Flask's `render_template()` looks in a folder called
`templates` by default — that's a Flask convention, not something we chose
arbitrarily.

## `Script/script.js`

Four functions do everything:

**`sendMessage()`** — reads the input box, immediately shows your message
(`addMessage(message, "user")`), shows a typing indicator, then does:
```javascript
fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: message })
})
```
This is the only place the frontend "talks AI" — and even then, it's only
ever talking to your own Flask server, never to Google directly.

**`addMessage(text, type)`** — builds a message bubble and appends it to the
`#messages` div. `type` is `"user"` or `"ai"`, which controls the CSS class
(and therefore which side it's aligned to, what color it is).

**`addTyping()` / `removeTyping()`** — show/hide the bouncing-dots bubble
while waiting for the server to respond, so the UI doesn't feel frozen.

**The `keydown` listener** — lets Enter submit, same as clicking Send.

Notice what's *not* here: no API keys, no mention of Gemini, no prompt text.
The frontend doesn't know or care what's answering it — it only knows how to
POST a string and render a string back. That's intentional, and it's why you
can swap the backend's AI provider entirely without touching this file.

## `Styles/styles.css`

Pure appearance — CSS variables at the top (`--violet`, `--teal`, `--bg-deep`,
etc.) control the whole palette from one place, so retheming means editing a
handful of lines instead of hunting through the file.

## The one rule worth remembering

**If it involves the AI's behavior, it belongs in `persona.py` or `tools.py`
on the server — never in the frontend.** The frontend is a dumb display
layer on purpose. Keeping it that way is what makes the backend swappable
and the API key safe.

Next: [04-build-your-own.md](./04-build-your-own.md)
