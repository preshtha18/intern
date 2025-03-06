import streamlit as st
import requests
import json

TOGETHER_API_KEY = "9a9c677350c80c2a755ab1e3f3399f10de45f36bc60084495908cb2b4835f94a"
API_URL = "https://api.together.xyz/v1/chat/completions"

st.title("AI Chatbot using Together API")
st.write("Powered by an open-source model")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.text_input("Ask me anything:", "")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    payload = {
        "model": "mistralai/Mistral-7B-Instruct-v0.2",
        "messages": st.session_state.messages,
        "temperature": 0.7,
        "max_tokens": 256
    }
    headers = {"Authorization": f"Bearer {TOGETHER_API_KEY}"}

    response = requests.post(API_URL, headers=headers, json=payload)
    print(response.json())  # Debugging

    bot_response = response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
    if not bot_response:
        bot_response = "Sorry, I couldn't process that."

    st.session_state.messages.append({"role": "assistant", "content": bot_response})

    with st.chat_message("assistant"):
        st.markdown(bot_response)
