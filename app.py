from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)  # allow cross-origin requests from frontend

knowledge = {
    "who are you": "I am DaxAI, your advanced AI assistant.",
    "what is your name": "My name is DaxAI.",
    "who is alan turing": (
        "Alan Turing was a British mathematician and computer scientist, "
        "considered the father of theoretical computer science and artificial intelligence."
    ),
    "what is python": (
        "Python is a high-level, interpreted programming language known for its readability and versatility."
    ),
    "tell me a joke": "Why did the computer show up at work late? Because it had a hard drive!",
    "help": "You can ask me about famous people, programming, or ask for a joke!"
}

def normalize(text):
    return re.sub(r'[^\w\s]', '', text.lower()).strip()

def get_response(text):
    text_norm = normalize(text)

    # Exact knowledge base match
    if text_norm in knowledge:
        return knowledge[text_norm]

    # Simple intent detection
    if "weather" in text_norm:
        return "I can't fetch live weather data yet, but I hope it's nice where you are!"
    if any(greet in text_norm for greet in ["hello", "hi", "hey"]):
        return "Hello! How can I assist you today?"
    if any(bye in text_norm for bye in ["bye", "goodbye"]):
        return "Goodbye! Have a great day!"

    # Fallback
    return "I'm still learning. Could you ask something else?"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    user_text = data.get("text", "")
    response = get_response(user_text)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
