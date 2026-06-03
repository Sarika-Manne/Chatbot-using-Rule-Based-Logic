def chatbot():
    print("🤖 ChatBot: Hello! I am RuleBot.")
    print("Type 'bye' to exit.")

    responses = {
        "hi": "Hello! How can I help you?",
        "hello": "Hi there!",
        "how are you": "I am doing great. Thanks for asking!",
        "what is your name": "My name is RuleBot.",
        "who created you": "I was created using Python.",
        "what is python": "Python is a popular programming language.",
        "what can you do": "I can answer simple questions and greetings.",
        "help": "You can ask me about Python, my name, or greetings."
    }

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "bye":
            print("🤖 ChatBot: Goodbye! Have a great day!")
            break

        elif user_input in responses:
            print("🤖 ChatBot:", responses[user_input])

        else:
            print("🤖 ChatBot: Sorry, I don't understand that question.")

chatbot()