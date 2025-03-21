import nltk
import random
from nltk.chat.util import Chat, reflections

# Download NLTK resources (if you haven't already)
nltk.download('punkt')

# Define chatbot patterns and responses
chatbot_patterns = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I assist you today?"]),
    (r"how are you?", ["I'm doing well, thank you!", "I'm good, how about you?", "I'm fine, how can I help you?"]),
    (r"what is your name?", ["I am a chatbot. You can call me Bot.", "I don't have a name, but you can call me Bot."]),
    (r"bye|goodbye", ["Goodbye! Take care!", "See you later!", "Bye! Have a great day!"]),
    (r"tell me a joke", ["Why don't scientists trust atoms? Because they make up everything!", "Why did the chicken join a band? Because it had drumsticks!"]),
    (r"(.*)", ["I'm not sure how to respond to that, but I can try to help!", "Can you rephrase that? I'm not sure I understand."])
]

# Create a chatbot instance
chatbot = Chat(chatbot_patterns, reflections)

def start_chat():
    print("Hello! I'm your chatbot. Type 'bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'goodbye']:
            print(random.choice(chatbot_patterns[3][1]))
            break
        response = chatbot.respond(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    start_chat()
