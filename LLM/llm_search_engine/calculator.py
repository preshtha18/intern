import requests

TOGETHER_API_KEY = "b812f285adf790e40aebdd7024e79f6101aaff5e06e4cdb21ec293090c15486c"


def calculator_together_api():
    """Takes a math expression as input and evaluates it using the Together API."""
    expression = input("Enter a mathematical expression to calculate: ")

    url = "https://api.together.xyz/v1/completions"
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mistralai/Mistral-7B-Instruct-v0.2",
        "prompt": f"Calculate the result of: {expression}",
        "temperature": 0,
        "max_tokens": 50
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print("\nCalculation Result:\n")
        print(response.json()["choices"][0]["text"].strip())
    else:
        print(f"Error: {response.json()}")


calculator_together_api()
