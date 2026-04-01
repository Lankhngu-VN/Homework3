n = int(input())
if n <= 0:
    print("NO")
else:
    while n % 3 == 0:
        n //= 3
    if n == 1:
        print("YES")
    else:
        print("NO")