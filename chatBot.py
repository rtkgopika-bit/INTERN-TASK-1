def chatbot():
    print("Hello! I am your personal chatbot🤗,Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input == "quit":
            print("Chatbot: Goodbye😊🙏🏻! Have a great day!")
            break
        
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello there😊! How can I help you today?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program😊, but I'm feeling great! How about you?")
        elif "your name" in user_input:
            print("Chatbot: I am a simple Python chatbot.You can call me ChatPy😇")
        elif "tata!bye" in user_input:
            print("Chatbot: okay byee👋🏻!thanks for chatting me✨")
        else:
            print("Chatbot: Sorry, I don't understand that,Can you ask something else💭quit?")
        
        
        
if __name__ == "__main__":
    chatbot()


