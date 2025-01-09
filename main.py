import cohere

# Replace 'your-api-key' with your actual API key from Cohere
API_KEY = 'cEKBXBGyOUdlb7d5Ei4rXEoptMlT0zSnJ0IaUg84'

# Initialize the Cohere client
co = cohere.Client(API_KEY)


print("========================================")
print("       Welcome to the Chatbot!          ")
print("========================================")
print("\nChatbot: Hello! I'm your virtual assistant. Type 'bye' to exit.")

conversation_history = ""  # Keeps track of the conversation history

while True:
    # Get user input
    user_input = input("You: ")

    # Exit condition
    if user_input.lower() == 'exit':
        print("Cohere Chatbot: Goodbye! Have a great day!")
        break

        # Update the conversation history
    conversation_history += f"User: {user_input}\nAssistant:"

    # Send the input to the Cohere API
    response = co.generate(
        model='command-xlarge-nightly',  # Specify the model
        prompt=conversation_history,
        max_tokens=100,                  # Adjust the maximum response length
        temperature=0.7,                 # Adjust creativity
    )

    # Extract and print the AI's response
    ai_response = response.generations[0].text.strip()
    print(f"Cohere Chatbot: {ai_response}")

    # Append the AI's response to the conversation history
    conversation_history += f" {ai_response}\n"
