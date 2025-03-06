import streamlit as st
import requests
import json

TOGETHER_API_KEY = "9a9c677350c80c2a755ab1e3f3399f10de45f36bc60084495908cb2b4835f94a"
API_URL = "https://api.together.xyz/v1/chat/completions"

st.title("AI Document Summarizer")
st.write("Summarize long documents efficiently with AI!")

user_input = st.text_area("Paste your document text below:", height=300)

summary_length = st.selectbox(
    "Select summary length:",
    ["Short", "Medium", "Detailed"]
)

if st.button("Summarize"):
    if user_input.strip():
        system_prompt = f"You are an AI assistant that summarizes long documents. Provide a {summary_length.lower()} summary of the given text."

        payload = {
            "model": "mistralai/Mistral-7B-Instruct-v0.2",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            "temperature": 0.5,
            "max_tokens": 400
        }

        headers = {"Authorization": f"Bearer {TOGETHER_API_KEY}"}

        response = requests.post(API_URL, headers=headers, json=payload)

        summarized_text = response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
        if not summarized_text:
            summarized_text = "Sorry, I couldn't summarize the document. Try again with a different input."

        st.subheader(f"Generated {summary_length} Summary:")
        st.write(summarized_text)
    else:
        st.warning("Please enter text to summarize.")
