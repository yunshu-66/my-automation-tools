# greet 函数：用于向用户打招呼，打印问候语
def greet():
    print("你好！欢迎使用本程序。")

# add 函数：接收两个数字，返回它们的和
def add(a, b):
    return a + b

name='yunshu'
age='21'
print("我的名字是",name,"今年",age,"岁")
score=50
if score>=60:
    print("及格")
else:
    print("不及格")
for i in range(5):
    print("第",i,"次")
total=0
for i in range(1,100):
    total=total+i
print("1加到100等于",total)
