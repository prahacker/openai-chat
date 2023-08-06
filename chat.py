import openai

# Replace 'YOUR_OPENAI_API_KEY' with your actual GPT-3 API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Function to generate a response using GPT-3 model
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        stop=["\n"],
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Function to interact with the chatbot
def chat_with_bot():
    print("Chatbot: Hello! I'm here to chat with you. Type 'exit' or 'bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "bye"]:
            print("Chatbot: Goodbye! Have a great day.")
            break
        else:
            response = generate_response(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    chat_with_bot()
