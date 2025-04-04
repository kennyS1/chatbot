import requests

API_KEY = "you-api"
API_URL = "https://api.deepseek.com/v1/chat/completions"

def chat_with_deepseek(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        return f"Error: {response.status_code}, {response.text}"

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_deepseek(user_input)
        print("Chatbot:", response)

