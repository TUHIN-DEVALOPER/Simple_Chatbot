import random

var = input("You : ").lower()

if var == "hello":
    hello_responses = [
        "Hello! How can I assist you today?",
        "Hi there! What can I do for you?",
        "Hey! Need any help?",
        "Greetings! How may I assist you?",
        "Hello! Feel free to ask me anything.",
        "Hi! I'm here to help.",
        "Hey there! What’s on your mind?"
    ]
    bot = random.choice(hello_responses)
    print(f"Bot: {bot}")
elif var == "what is programming":
    programming_responses = [
        "Programming is all about problem-solving and creativity!",
        "Python is a great language for beginners and professionals alike.",
        "Debugging is just as important as writing code!",
        "Always write clean and readable code.",
        "Algorithms and data structures are key to efficient programming.",
        "Practice makes perfect in programming!",
        "Open-source contributions help you learn and grow as a developer.",
        "Version control systems like Git are essential for developers.",
        "Automate repetitive tasks with Python scripts!",
        "Learning a new programming language expands your thinking."
    ]
    bot = random.choice(programming_responses)
    print(f"Bot: {bot}")
else:
    print("I am Simple Chatbot")