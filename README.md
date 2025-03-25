# 🤖 Simple Chatbot

A basic chatbot implemented in Python that responds to user inputs with predefined messages.

## ✨ Features
- ✅ Simple text-based interaction.
- 🎲 Randomized responses for variety.
- 💬 Handles greetings and basic programming-related queries.
- ❓ Provides a default response for unknown inputs.

## 🚀 Installation & Usage
### 📌 Prerequisites
- 🐍 Python 3.x installed on your system.

### ▶️ Running the Chatbot
1. 📥 Clone this repository or download the script.
2. 🖥️ Open a terminal or command prompt.
3. 🔧 Run the script using:
   ```bash
   python chatbot.py
   ```
4. 💬 Type a message and interact with the chatbot!

## 💡 Example Usage
```
You: hello
Bot: Hey! Need any help?
```
```
You: what is programming
Bot: 🖥️ Algorithms and data structures are key to efficient programming.
```
```
You: how are you?
Bot: 🤖 I am Simple Chatbot
```

## 🛠️ Code Overview
The chatbot follows a simple structure:
- 🏗️ Takes user input.
- 🔍 Checks for predefined keywords (`hello`, `what is programming`).
- 🎲 Responds with a randomly chosen message from a predefined list.
- ❓ Returns a default response if the input is not recognized.

### 📝 Code Snippet
```python
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
```

## 🔮 Future Improvements
- ➕ Add more responses to cover a wider range of topics.
- 🤖 Implement NLP techniques for more natural conversation.
- 📲 Integrate with a web or mobile application.

## 📜 License
This project is open-source and free to use under the MIT License.
