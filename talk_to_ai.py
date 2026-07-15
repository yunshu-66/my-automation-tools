import requests

def ask_ai(prompt):
    api_key = "你的DEEPSEEK_API_KEY"
    url = "https://api.deepseek.com/chat/completions"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}]
    }
    r = requests.post(url, headers=headers, json=data)
    return r.json()["choices"][0]["message"]["content"]

# 测试
print(ask_ai("用一句话解释什么是人工智能"))
