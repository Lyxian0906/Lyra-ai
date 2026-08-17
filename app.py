import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify, send_from_directory
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

app = Flask(__name__, template_folder="templates")


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

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=message
        )
        return jsonify({"response": response.text})
    except Exception as e:
        print("Gemini error:", e)
        return jsonify({"response": "Lyra hit an error talking to the model. Check the server logs."}), 500


if __name__ == "__main__":
    app.run(debug=True)