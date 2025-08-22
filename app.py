from flask import Flask, request, jsonify, send_from_directory
import openai

app = Flask(__name__, static_folder="static")

# ⚠️ Your OpenAI API key (keep private!)
openai.api_key = "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"

# Serve index.html
@app.route("/")
def index():
    return send_from_directory("static", "index.html")

# General AI chat
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "")
    if not message:
        return jsonify({"reply": "Please provide a message."})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": message}],
            temperature=0.7,
            request_timeout=30
        )
        reply = response.choices[0].message.content
    except Exception as e:
        reply = f"Error: {str(e)}"

    return jsonify({"reply": reply})

# Generate Website
@app.route("/generate-site", methods=["POST"])
def generate_site():
    data = request.json
    idea = data.get("idea", "")
    prompt = f"Create a complete HTML/CSS/JS website for this idea:\n{idea}\nReturn only the code inside a code block."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            request_timeout=60
        )
        code = response.choices[0].message.content
    except Exception as e:
        code = f"Error: {str(e)}"

    return jsonify({"code": code})

# Generate Discord Bot
@app.route("/generate-bot", methods=["POST"])
def generate_bot():
    data = request.json
    idea = data.get("idea", "")
    prompt = f"Create a Discord bot using Python (discord.py) for this task:\n{idea}\nReturn only the Python code."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            request_timeout=60
        )
        bot_code = response.choices[0].message.content
    except Exception as e:
        bot_code = f"Error: {str(e)}"

    return jsonify({"bot_code": bot_code})

# Generate Any Code
@app.route("/generate-any-code", methods=["POST"])
def generate_any_code():
    data = request.json
    idea = data.get("idea", "")
    prompt = f"Write code for the following task:\n{idea}\nReturn only the code."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            request_timeout=60
        )
        code = response.choices[0].message.content
    except Exception as e:
        code = f"Error: {str(e)}"

    return jsonify({"code": code})

if __name__ == "__main__":
    app.run(debug=True)
