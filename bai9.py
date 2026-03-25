a = int(input())
b=False
for i in range(1, a+1):
    if i*i==a:
        b=True
        break
    elif i*i>a:
        break
if b:
    print("Yes")
else:
    print("No")