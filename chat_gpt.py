import openai

# Replace with your OpenAI API key
openai.api_key = "your-api-key-here"

# Initialize the conversation
messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

print("Chat with ChatGPT! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in {"exit", "quit"}:
        print("Goodbye!")
        break

    # Add user message
    messages.append({"role": "user", "content": user_input})

    # Get assistant reply
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4"
            messages=messages
        )
        reply = response['choices'][0]['message']['content']
        print("ChatGPT:", reply)

        # Add assistant reply to messages
        messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        print("Error:", e)
