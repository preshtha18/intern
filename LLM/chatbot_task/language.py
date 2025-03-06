import streamlit as st
import requests
import json

TOGETHER_API_KEY = "9a9c677350c80c2a755ab1e3f3399f10de45f36bc60084495908cb2b4835f94a"
API_URL = "https://api.together.xyz/v1/chat/completions"

st.title("AI Language Translator")
st.write("Translate text into multiple languages with AI!")

user_input = st.text_area("Enter the text to translate:", "")

target_language = st.selectbox(
    "Select the target language:",
    ["French", "Spanish", "German", "Chinese", "Japanese", "Italian", "Hindi"]
)

if st.button("Translate"):
    if user_input.strip():
        system_prompt = f"You are an AI language translator. Translate the following text into {target_language}."

        payload = {
            "model": "mistralai/Mistral-7B-Instruct-v0.2",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            "temperature": 0.7,
            "max_tokens": 250
        }

        headers = {"Authorization": f"Bearer {TOGETHER_API_KEY}"}

        response = requests.post(API_URL, headers=headers, json=payload)

        translated_text = response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
        if not translated_text:
            translated_text = "Sorry, I couldn't translate the text. Try again with a different input."

        st.subheader(f"Translated Text ({target_language}):")
        st.write(translated_text)
    else:
        st.warning("Please enter text to translate.")
