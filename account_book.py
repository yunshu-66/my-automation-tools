import os

data_file = "D:/我的窝计划/记账本/records.txt"

# 确保数据文件存在
if not os.path.exists(data_file):
    open(data_file, "w", encoding="utf-8").close()

def add_record():
    category = input("类别（吃饭/交通/娱乐…）：")
    amount = input("金额：")
    note = input("备注：")
    with open(data_file, "a", encoding="utf-8") as f:
        f.write(category + "," + amount + "," + note + "\n")
    print("已记录 ✓")

def view_records():
    with open(data_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    if len(lines) == 0:
        print("还没有任何记录")
        return
    total = 0
    for line in lines:
        parts = line.strip().split(",")
        print("类别:", parts[0], "金额:", parts[1], "备注:", parts[2])
        total += float(parts[1])
    print("总支出：", total)

while True:
    print("\n==== 我的记账本 ====")
    print("1. 记一笔   2. 查看记录   3. 退出")
    choice = input("选：")
    if choice == "1":
        add_record()
    elif choice == "2":
        view_records()
    elif choice == "3":
        print("再见")
        break
    else:
        print("输入无效，重选")
