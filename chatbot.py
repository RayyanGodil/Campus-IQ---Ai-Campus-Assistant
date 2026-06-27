from groq import Groq
from campus_data import CAMPUS_INFO

client = Groq(api_key="enter api key here")

conversation_history = [
    {"role": "system", "content": CAMPUS_INFO}
]

print("=" * 40)
print("🎓 Campus IQ")
print("=" * 40)
print("Ask me anything about campus!")
print("Type 'quit' to exit.\n")

while True:
    user_input = input("You: ").strip()

    if not user_input:
        continue

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    conversation_history.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=conversation_history
        )
        reply = response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": reply})
        print(f"\nAssistant: {reply}\n")
    except Exception as e:
        print(f"Error: {e}\n")