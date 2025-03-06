from http.client import responses

import requests
import os

TOGETHER_API_KEY = "b812f285adf790e40aebdd7024e79f6101aaff5e06e4cdb21ec293090c15486c"


def search_together_api():
    """Takes user input dynamically and fetches search results using Together API."""
    query = input("Enter your search query: ")
    url = "https://api.together.xyz/v1/completions"
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mistralai/Mistral-7B-Instruct-v0.2",
        "prompt": f"Search the web and summarize the latest information about: {query}",
        "temperature": 0.7,
        "max_tokens": 500
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print("\nSearch Results:\n")
        print(response.json()["choices"][0]["text"])
    else:
        print(f"Error: {response.json()}")

search_together_api()