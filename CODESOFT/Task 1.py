import re

def respond_to_user_input(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Greetings
    if re.search(r'\b(hi|hello|hey)\b', user_input):
        return "Hello! How can I assist you today?"

    # Weather inquiries
    elif re.search(r'\b(weather|forecast)\b', user_input):
        return "The weather is sunny today."

    # Default response for unknown queries
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase or ask something else?"

# Simple conversation loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
        print("Goodbye!")
        break

    response = respond_to_user_input(user_input)
    print("Chatbot:", response)
