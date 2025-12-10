from ollama import chat

response = chat(
    model="smollm2:1.7b",
    messages=[
        {
            "role": "user",
            "content": "Why is the sky blue?"
        }
    ]
)

print(response.message.content)