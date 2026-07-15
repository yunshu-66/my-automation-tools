import requests

def ask_ai(prompt):
    api_key = "你的DEEPSEEK_API_KEY"   # 本地跑用真的；push 时再换成占位符
    url = "https://api.deepseek.com/chat/completions"
    headers = {"Authorization": "Bearer " + api_key, "Content-Type": "application/json"}
    data = {"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}]}
    r = requests.post(url, headers=headers, json=data)
    return r.json()["choices"][0]["message"]["content"]

# 假设这是 1000 条用户反馈里的 3 条（实际可以读文件循环）
feedbacks = [
    "网站打不开，我付了钱没下单", "几点开门", "很好用"
]

for text in feedbacks:
    # 1. 代码自己问 AI：这条是紧急还是普通？
    answer = ask_ai("只回答'紧急'或'普通'：" + text)

    # 2. 代码自己根据 AI 的回答，决定写到哪个文件
    if "紧急" in answer:
        with open("紧急.txt", "a", encoding="utf-8") as f:
            f.write(text + "\n")
        print("紧急 →", text)
    else:
        with open("常规.txt", "a", encoding="utf-8") as f:
            f.write(text + "\n")
        print("常规 →", text)
