name='yunshu'
count=30
print("我是",name,"，今天打算写",count,"行代码")
temperature=29
if temperature>=30:
    print("太热了")
if temperature<15:
    print("有点冷")
if 30>temperature>=15:
    print("舒服")
for i in range(1,21):
    if i%2==0:
        print(i)
total=0
for i in range(1,101):
    if i%2==0:
        total=total+i
print(total)
n=0
for i in range(1,51):
    if i%7==0:
        n=n+1
print("1到50中能被7整除的数有",n,"个")