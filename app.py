from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("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")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    # send message to GPT
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",   # faster & cheaper, still smart
        messages=[{"role": "user", "content": user_message}]
    )

    bot_reply = response["choices"][0]["message"]["content"]
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
