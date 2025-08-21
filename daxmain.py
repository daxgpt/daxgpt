class DaxAI:
    def __init__(self):
        self.knowledge = {
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
            "help": (
                "You can ask me about famous people, programming, or ask for a joke!"
            )
        }

    def get_response(self, text):
        text = text.lower().strip(" ?!")
        # Exact match
        if text in self.knowledge:
            return self.knowledge[text]
        # Keyword matching
        if "weather" in text:
            return "I can't fetch live weather data yet, but I hope it's nice where you are!"
        if "hello" in text or "hi" in text or "hey" in text:
            return "Hello! How can I assist you today?"
        if "bye" in text or "goodbye" in text:
            return "Goodbye! Have a great day!"
        # Default fallback
        return "I'm still learning. Could you ask something else?"

def main():
    ai = DaxAI()
    print("Welcome to DaxAI! (Ctrl+C to quit)")
    while True:
        try:
            user_input = input("You: ")
            response = ai.get_response(user_input)
            print("DaxAI:", response)
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
