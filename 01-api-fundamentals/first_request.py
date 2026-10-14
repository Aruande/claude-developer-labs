
# My first Claude API request
# Day 1 - Claude Developer Foundations

model = "claude-sonnet-4-5"
max_tokens = 100

message = {
    "role": "user",
    "content": "Explain what cloud computing is in one sentence."
}

print("Model:", model)
print("User message:", message["content"])
print("Message role:", message["role"])

messages = [
    {
        "role": "user",
        "content": "What is Amazon EC2?"
    },
    {
        "role": "assistant",
        "content": "Amazon EC2 provides virtual servers in the AWS cloud."
    },
    {
        "role": "user",
        "content": "How is that different from Lambda?"
    },
    {
        "role": "assistant",
        "content": "Lambda is a serverless compute service that runs code in response to events and automatically manages the underlying compute resources."
    }
]

print("First message:", messages[0]["content"])
print("Second message role:", messages[1]["role"])
print("Third message:", messages[2]["content"])
print("Fourth message:", messages[3]["content"])

request = {
    "model": model,
    "max_tokens": max_tokens,
    "messages": messages
}

print("\n--- Claude API Request ---")
print("Model:", request["model"])
print("Max tokens:", request["max_tokens"])
print("Number of messages:", len(request["messages"]))