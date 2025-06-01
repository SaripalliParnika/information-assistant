import sounddevice as sd
import queue
import sys
import json
from vosk import Model, KaldiRecognizer
from datetime import datetime
import wikipedia

q = queue.Queue()
output = ""

# Wikipedia
def ask_wikipedia(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your question is too broad. Did you mean: {e.options[0]}?"
    except wikipedia.exceptions.PageError:
        return "Sorry, I am not able to understand. Can you elaborate it?"
    except Exception as e:
        return f"An error occurred: {str(e)}"


# Handling user commands and assistant responses
def process_command(command):
    global output
    output = "" 
    command = command.lower()

    if "hello" in command or "hey" in command or "hi" in command:
        response = "Hello! How can I help you?"
    elif "time" in command:
        now = datetime.now().strftime("%H:%M:%S")
        response = f"Current time is {now}"
    elif "date" in command:
        today = datetime.now().strftime("%Y-%m-%d")
        response = f"Today's date is {today}"
    elif "exit" in command or "quit" in command:
        response = "Exiting. Goodbye!"
        return False
    else:
        response = ask_wikipedia(command)

    print(f"Assistant: {response}")
    output = response
    return output

# Text interface
def run_text_mode():
    print("Text mode activated. Type your question (type 'exit' to quit).")
    running = True
    while running:
        user_input = input("You: ")
        running = process_command(user_input)


def main():
        run_text_mode()


process_command.output = output

if __name__ == "__main__":
    main()
