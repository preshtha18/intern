import streamlit as st
import requests
import json

TOGETHER_API_KEY = "9a9c677350c80c2a755ab1e3f3399f10de45f36bc60084495908cb2b4835f94a"
API_URL = "https://api.together.xyz/v1/chat/completions"

st.title("📝 AI Content Generator")
st.write("Generate articles, stories, emails, and marketing content with AI!")

content_type = st.selectbox(
    "Choose the type of content to generate:",
    ["Article", "Story", "Email", "Marketing Copy"]
)

# User input prompt
user_input = st.text_area("Describe what you want:", "")

if st.button("Generate Content"):
    if user_input.strip():
        system_prompt = f"You are an AI content writer. Generate a high-quality {content_type.lower()} based on the user's input."

        payload = {
            "model": "mistralai/Mistral-7B-Instruct-v0.2",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            "temperature": 0.8,
            "max_tokens": 500
        }

        headers = {"Authorization": f"Bearer {TOGETHER_API_KEY}"}

        response = requests.post(API_URL, headers=headers, json=payload)

        bot_response = response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
        if not bot_response:
            bot_response = "Sorry, I couldn't generate content. Try again with a different prompt."

        st.subheader(f"Generated {content_type}:")
        st.write(bot_response)
    else:
        st.warning("Please enter a description for your content.")
