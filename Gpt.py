from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model ="gpt-4o",
    messages=[
        {
            "role": "user",
            "content" : "Hello! How are you?"
        }
    ]
)

print (response.choices[0].message.content)