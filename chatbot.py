def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! dude! How can I help you today?"

    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking "

    elif "your name please" in user_input:
        return "I am a chatbot."

    elif "help" in user_input:
        return "Sure! I can answer your questions. "

    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a nice day "

    else:
        return "Sorry, I didn't understand that. Can you try something else?"

# Chat loop
print("Chatbot: Hello! Type 'bye' to end the conversation.")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Chatbot:", response)

    if "bye" in user_input.lower() or "exit" in user_input.lower():
        break
