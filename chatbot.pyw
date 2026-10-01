import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime

# ---------------- CHATBOT RESPONSES ----------------

responses = {
    "hello": "Hello! How are you?",
    "hi": "Hi! How can I help you?",
    "hey": "Hey! Nice to meet you.",
    
    "how are you": "I am doing great! How can I help you today?",
    
    "your name": "My name is Chatbot. I am a simple rule-based chatbot.",
    "name": "My name is Chatbot. I am a simple rule-based chatbot.",
    "who are you": "I am a lightweight rule-based chatbot created using Python.",
    
    "help": "You can ask me about Python, study, projects, time, or general greetings.",
    
    "study": "Regular practice is the key to success. Keep learning and stay consistent.",
    
    "project": "A good project should be divided into small and manageable parts.",
    
    "python": "Python is a popular and beginner-friendly programming language.",
    
    "thank you": "You're welcome! Happy to help.",
    "thanks": "You're welcome!",
    
    "bye": "Goodbye! Have a great day!"
}


# ---------------- CHATBOT LOGIC ----------------

def get_response(message):
    message = message.lower().strip()

    if "time" in message:
        return "The current time is " + datetime.now().strftime("%I:%M:%S %p")

    for keyword, answer in responses.items():
        if keyword in message:
            return answer

    return "Sorry, I don't understand that yet. Please type 'help' to see what I can answer."


# ---------------- SEND MESSAGE ----------------

def send_message(event=None):
    message = entry.get().strip()

    if not message:
        return

    chat_box.config(state=tk.NORMAL)

    chat_box.insert(
        tk.END,
        "You: " + message + "\n",
        "user"
    )

    answer = get_response(message)

    chat_box.insert(
        tk.END,
        "Chatbot: " + answer + "\n\n",
        "bot"
    )

    chat_box.config(state=tk.DISABLED)
    chat_box.see(tk.END)

    entry.delete(0, tk.END)


# ---------------- CLEAR CHAT ----------------

def clear_chat():
    chat_box.config(state=tk.NORMAL)
    chat_box.delete("1.0", tk.END)

    chat_box.insert(
        tk.END,
        "Chatbot: Hello! I am your personal chatbot.\n"
        "Chatbot: Type 'help' to see what I can do.\n\n",
        "bot"
    )

    chat_box.config(state=tk.DISABLED)


# ---------------- GUI WINDOW ----------------

root = tk.Tk()

root.title("Chatbot - Lightweight AI Chatbot")
root.geometry("750x650")
root.minsize(550, 500)


# Title

title = tk.Label(
    root,
    text="🤖 Chatbot",
    font=("Arial", 25, "bold")
)

title.pack(pady=(15, 3))


subtitle = tk.Label(
    root,
    text="Lightweight Rule-Based Chatbot • No API • No Model",
    font=("Arial", 10)
)

subtitle.pack(pady=(0, 10))


# Chat box

chat_box = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    font=("Arial", 12),
    state=tk.DISABLED
)

chat_box.pack(
    padx=20,
    pady=10,
    fill=tk.BOTH,
    expand=True
)


# Text styles

chat_box.tag_config(
    "user",
    font=("Arial", 12, "bold")
)

chat_box.tag_config(
    "bot",
    font=("Arial", 12)
)


# Welcome message

chat_box.config(state=tk.NORMAL)

chat_box.insert(
    tk.END,
    "Chatbot: Hello! I am your personal chatbot.\n"
    "Chatbot: How can I help you today?\n"
    "Chatbot: Type 'help' to see what I can do.\n\n",
    "bot"
)

chat_box.config(state=tk.DISABLED)


# ---------------- INPUT AREA ----------------

bottom_frame = tk.Frame(root)

bottom_frame.pack(
    fill=tk.X,
    padx=20,
    pady=15
)


entry = tk.Entry(
    bottom_frame,
    font=("Arial", 13)
)

entry.pack(
    side=tk.LEFT,
    fill=tk.X,
    expand=True,
    ipady=10
)


# Send button

send_button = tk.Button(
    bottom_frame,
    text="Send ➤",
    font=("Arial", 11, "bold"),
    command=send_message,
    padx=18,
    pady=8
)

send_button.pack(
    side=tk.LEFT,
    padx=(8, 0)
)


# Clear button

clear_button = tk.Button(
    root,
    text="Clear Chat",
    font=("Arial", 10),
    command=clear_chat
)

clear_button.pack(
    pady=(0, 15)
)


# Enter key

entry.bind(
    "<Return>",
    send_message
)

entry.focus()


# Start chatbot

root.mainloop()