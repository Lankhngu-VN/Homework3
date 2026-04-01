n = int(input())
A = True
if n <=0 :
    A = False
for i in range(1, n+1):
    if 3**i == n:
        A = True
        break
    else:
        A = False
if A:
    print("YES")
else:
    print("NO")