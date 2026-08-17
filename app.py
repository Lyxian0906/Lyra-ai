import os
import json
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify, send_from_directory
from google import genai
from google.genai import types
from persona import SYSTEM_PROMPT
from tools import get_current_time, get_project_status, get_lyx_info

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

app = Flask(__name__, template_folder="templates")

#Chat hisotry
HISTORY_FILE = "conversation.json"

# Add new functions to tools.py, then list them here.
LYRA_TOOLS = [get_current_time, get_project_status, get_lyx_info]

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []


def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/Script/<path:filename>")
def script_files(filename):
    return send_from_directory("Script", filename)


@app.route("/Styles/<path:filename>")
def style_files(filename):
    return send_from_directory("Styles", filename)


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "").strip()

    if not message:
        return jsonify({"response": "Say something and I'll answer."}), 400

    history = load_history()
    history.append({"role": "user", "text": message})

    # Convert saved history into the format the Gemini API expects
    contents = [
        {"role": turn["role"], "parts": [{"text": turn["text"]}]}
        for turn in history
    ]

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT
            )
        )
        reply = response.text
        history.append({"role": "model", "text": reply})
        save_history(history)
        return jsonify({"response": reply})
    except Exception as e:
        print("Gemini error:", e)
        return jsonify({"response": "Lyra hit an error talking to the model. Check the server logs."}), 500


@app.route("/reset", methods=["POST"])
def reset():
    save_history([])
    return jsonify({"status": "cleared"})


if __name__ == "__main__":
    app.run(debug=True)