'''def chatbot():
    while True:
        user = input("You: ").lower()
        if "Hello" in user:
            print("Bot: Hi there!")
        elif "How are you" in user:
            print("Bot:  I am doing great, thanks!")
        elif "bye" in user:
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

        chatbot()
        '''

def chatbot():
    print("Hello! I'm your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a nice day.")
            break
        else:
            print("Chatbot: You said -", user_input)


# Run the chatbot
if __name__ == "__main__":
    chatbot()
