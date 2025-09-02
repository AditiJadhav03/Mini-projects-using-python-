"""
chatbot_fuzzy.py
A simple fuzzy-matching chatbot using RapidFuzz.
Save as chatbot_fuzzy.py and run: python chatbot_fuzzy.py
"""

import re
import random
from rapidfuzz import process, fuzz
from datetime import datetime

# ---------------------------
# 1) Knowledge base (patterns -> intent)
# ---------------------------
# Each intent has several example patterns (phrases users might type).
patterns = {
    "greeting": [
        "hi", "hello", "hey", "hey there", "good morning", "good evening", "hiya"
    ],
    "how_are_you": [
        "how are you", "how are you doing", "how's it going", "how you doing"
    ],
    "bot_name": [
        "what is your name", "who are you", "your name", "who am i talking to"
    ],
    "time": [
        "what time is it", "current time", "tell me the time", "time now"
    ],
    "date": [
        "what is the date", "today's date", "date today", "what day is it"
    ],
    "thanks": [
        "thanks", "thank you", "thx", "thank u"
    ],
    "bye": [
        "bye", "goodbye", "see you", "exit", "quit"
    ],
    "joke": [
        "tell me a joke", "make me laugh", "joke please"
    ],
    "help": [
        "help", "what can you do", "commands", "how to use"
    ],
}

# ---------------------------
# 2) Responses for each intent
# ---------------------------
responses = {
    "greeting": [
        "Hello!  How can I help you today?",
        "Hi there!  What would you like to talk about?"
    ],
    "how_are_you": [
        "I'm a program, so I don't have feelings — but I'm here for you! ",
        "Doing great — ready to help! "
    ],
    "bot_name": [
        "I'm PyBot, your friendly Python chatbot ",
        "You can call me PyBot!"
    ],
    "time": [
        lambda: f"The current time is {datetime.now().strftime('%H:%M:%S')} "
    ],
    "date": [
        lambda: f"Today's date is {datetime.now().strftime('%Y-%m-%d')} "
    ],
    "thanks": [
        "You're welcome! ",
        "No problem! Glad I could help."
    ],
    "bye": [
        "Goodbye! Have a great day!",
        "See you later! Take care "
    ],
    "joke": [
        "Why did the programmer quit his job? Because he didn't get arrays. ",
        "I would tell you a UDP joke, but you might not get it. "
    ],
    "help": [
        "I can answer greetings, tell time/date, tell a joke, or say goodbye. Try saying 'hi' or 'tell me a joke'!",
        "Try: 'hi', 'what time is it', 'tell me a joke', or 'bye'."
    ],
}

# ---------------------------
# 3) Build lookup structures
# ---------------------------
# Map example phrase -> intent so we can lookup the matched phrase's intent
phrase_to_intent = {}
for intent, phrase_list in patterns.items():
    for phrase in phrase_list:
        # store normalized phrase as key
        key = phrase.lower().strip()
        phrase_to_intent[key] = intent

# choices list used by RapidFuzz
choices = list(phrase_to_intent.keys())

# ---------------------------
# 4) Utility functions
# ---------------------------
def normalize(text: str) -> str:
    """
    Normalize the user text:
    - lowercasing
    - remove punctuation
    - collapse multiple spaces
    """
    text = text.lower().strip()
    # remove punctuation (keep words and numbers)
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text

def choose_response(intent: str):
    """
    Return a response (string). Responses can be strings or callables (to create dynamic responses).
    """
    options = responses.get(intent, ["Sorry, I don't know how to respond to that."])
    resp = random.choice(options)
    # if resp is callable (like time/date lambdas), call it
    return resp() if callable(resp) else resp

# ---------------------------
# 5) Chat loop
# ---------------------------
def chat():
    print("PyBot : Hello! I'm a fuzzy chatbot. Type 'bye' to exit.")
    print("Tip: ask in many different ways — I'll try to understand. (Try: 'how are you', 'what time is it', 'tell me a joke')\n")

    # open chat log to append conversations
    with open("chat_history.txt", "a", encoding="utf-8") as log:
        log.write(f"\n\n--- New session at {datetime.now()} ---\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            # ignore empty lines
            continue

        user_norm = normalize(user_input)

        # first check for exact 'bye' words quickly to allow immediate exit
        if any(word in user_norm.split() for word in ["bye", "goodbye", "exit", "quit"]):
            print("PyBot:", choose_response("bye"))
            with open("chat_history.txt", "a", encoding="utf-8") as log:
                log.write(f"You: {user_input}\nPyBot: {choose_response('bye')}\n")
            break

        # Use RapidFuzz to find the best matching known phrase
        # scorer - token_sort_ratio handles different word orders well
        best = process.extractOne(user_norm, choices, scorer=fuzz.token_sort_ratio)

        # best is a tuple: (matched_choice, score, index)
        if best:
            matched_phrase, score, _ = best
        else:
            matched_phrase, score = None, 0

        # threshold for acceptance - you can tune this (50-70 typical)
        THRESHOLD = 60

        if score >= THRESHOLD and matched_phrase in phrase_to_intent:
            intent = phrase_to_intent[matched_phrase]
            reply = choose_response(intent)
            print("PyBot:", reply)
            # log conversation
            with open("chat_history.txt", "a", encoding="utf-8") as log:
                log.write(f"You: {user_input}\nPyBot: {reply}\n")
        else:
            # fallback when bot is not confident
            print("PyBot: Sorry, I didn't understand. Can you rephrase or type 'help'? ")
            with open("chat_history.txt", "a", encoding="utf-8") as log:
                log.write(f"You: {user_input}\nPyBot: [fallback]\n")

if __name__ == "__main__":
    chat()



'''  
"""
chatbot_fuzzy.py
A simple fuzzy-matching chatbot using RapidFuzz.
Save as chatbot_fuzzy.py and run: python chatbot_fuzzy.py
"""

import re          # for cleaning/normalizing text (remove punctuation etc.)
import random      # for choosing random replies
from rapidfuzz import process, fuzz   # for fuzzy string matching (find closest user intent)
from datetime import datetime         # for dynamic time/date responses

# ---------------------------
# 1) Knowledge base (patterns -> intent)
# ---------------------------
# patterns = dictionary of possible user inputs for each "intent"
# intent = category of what user wants (greeting, time, joke, etc.)
patterns = {
    "greeting": [
        "hi", "hello", "hey", "hey there", "good morning", "good evening", "hiya"
    ],
    "how_are_you": [
        "how are you", "how are you doing", "how's it going", "how you doing"
    ],
    "bot_name": [
        "what is your name", "who are you", "your name", "who am i talking to"
    ],
    "time": [
        "what time is it", "current time", "tell me the time", "time now"
    ],
    "date": [
        "what is the date", "today's date", "date today", "what day is it"
    ],
    "thanks": [
        "thanks", "thank you", "thx", "thank u"
    ],
    "bye": [
        "bye", "goodbye", "see you", "exit", "quit"
    ],
    "joke": [
        "tell me a joke", "make me laugh", "joke please"
    ],
    "help": [
        "help", "what can you do", "commands", "how to use"
    ],
}

# ---------------------------
# 2) Responses for each intent
# ---------------------------
# responses = dictionary of possible answers chatbot gives for each intent
# Some responses are static (strings), some are dynamic (functions/lambdas for time/date)
responses = {
    "greeting": [
        "Hello! How can I help you today?",
        "Hi there!  What would you like to talk about?"
    ],
    "how_are_you": [
        "I'm a program, so I don't have feelings — but I'm here for you! ",
        "Doing great — ready to help! "
    ],
    "bot_name": [
        "I'm PyBot, your friendly Python chatbot ",
        "You can call me PyBot!"
    ],
    "time": [
        # dynamic reply - returns current time when called
        lambda: f"The current time is {datetime.now().strftime('%H:%M:%S')} "
    ],
    "date": [
        # dynamic reply - returns current date when called
        lambda: f"Today's date is {datetime.now().strftime('%Y-%m-%d')} "
    ],
    "thanks": [
        "You're welcome! ",
        "No problem! Glad I could help."
    ],
    "bye": [
        "Goodbye!  Have a great day!",
        "See you later! Take care "
    ],
    "joke": [
        "Why did the programmer quit his job? Because he didn't get arrays. ",
        "I would tell you a UDP joke, but you might not get it. "
    ],
    "help": [
        "I can answer greetings, tell time/date, tell a joke, or say goodbye. Try saying 'hi' or 'tell me a joke'!",
        "Try: 'hi', 'what time is it', 'tell me a joke', or 'bye'."
    ],
}

# ---------------------------
# 3) Build lookup structures
# ---------------------------
# We need a quick way to map user input → intent
phrase_to_intent = {}
for intent, phrase_list in patterns.items():
    for phrase in phrase_list:
        # normalize (lowercase, strip spaces) and save mapping
        key = phrase.lower().strip()
        phrase_to_intent[key] = intent

# Choices list = all possible phrases user might type
# RapidFuzz will compare user input with these
choices = list(phrase_to_intent.keys())

# ---------------------------
# 4) Utility functions
# ---------------------------
def normalize(text: str) -> str:
    """
    Normalize user input:
    - lowercase
    - remove punctuation
    - remove extra spaces
    """
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", "", text)  # keep only words/numbers
    text = re.sub(r"\s+", " ", text)    # collapse multiple spaces
    return text

def choose_response(intent: str):
    """
    Pick a random response for the intent.
    If response is a function (like time/date), call it before returning.
    """
    options = responses.get(intent, ["Sorry, I don't know how to respond to that."])
    resp = random.choice(options)
    return resp() if callable(resp) else resp   # call lambda if needed

# ---------------------------
# 5) Chat loop (main program)
# ---------------------------
def chat():
    print("PyBot : Hello! I'm a fuzzy chatbot. Type 'bye' to exit.")
    print("Tip: ask in many different ways — I'll try to understand. (Try: 'how are you', 'what time is it', 'tell me a joke')\n")

    # open chat log file to save history
    with open("chat_history.txt", "a", encoding="utf-8") as log:
        log.write(f"\n\n--- New session at {datetime.now()} ---\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue  # skip empty input

        user_norm = normalize(user_input)

        # if user says "bye"/"exit", quit immediately
        if any(word in user_norm.split() for word in ["bye", "goodbye", "exit", "quit"]):
            print("PyBot:", choose_response("bye"))
            with open("chat_history.txt", "a", encoding="utf-8") as log:
                log.write(f"You: {user_input}\nPyBot: {choose_response('bye')}\n")
            break

        # Fuzzy match input with known phrases
        best = process.extractOne(user_norm, choices, scorer=fuzz.token_sort_ratio)

        # best = (matched_phrase, score, index)
        if best:
            matched_phrase, score, _ = best
        else:
            matched_phrase, score = None, 0

        # Only accept match if score is above threshold
        THRESHOLD = 60

        if score >= THRESHOLD and matched_phrase in phrase_to_intent:
            # Find intent and reply
            intent = phrase_to_intent[matched_phrase]
            reply = choose_response(intent)
            print("PyBot:", reply)

            # Save conversation to log file
            with open("chat_history.txt", "a", encoding="utf-8") as log:
                log.write(f"You: {user_input}\nPyBot: {reply}\n")
        else:
            # Fallback if bot is unsure
            print("PyBot: Sorry, I didn't understand. Can you rephrase or type 'help'? ")
            with open("chat_history.txt", "a", encoding="utf-8") as log:
                log.write(f"You: {user_input}\nPyBot: [fallback]\n")

# Run chatbot if this file is executed directly
if __name__ == "__main__":
    chat()


'''