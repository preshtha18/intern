import os
from langchain_together import ChatTogether

os.environ["TOGETHER_API_KEY"] = "tgp_v1_JbcnM12r40Xik-LaQdcx7Zco_K9SjV6RwQ5lcfTbe5Y"

llm = ChatTogether(model="mistralai/Mixtral-8x7B-Instruct-v0.1", max_tokens=256, temperature=0.7)

chat_history = []

print("AI Chatbot (Type 'exit' to stop)")
while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    if user_input.lower() == "what was my first question?":
        if chat_history:
            print("Chatbot: Your first question was:", chat_history[0]["user"])
        else:
            print("Chatbot: You haven't asked any questions yet.")
        continue

    chat_history.append({"user": user_input})

    context = "\n".join([f"You: {msg['user']}\nChatbot: {msg.get('bot', '')}" for msg in chat_history])

    response = llm.invoke(f"{context}\nYou: {user_input}\nChatbot:")

    chat_history[-1]["bot"] = response

    print("Chatbot:", response)
