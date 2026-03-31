n = int(input())
k = 0
s = 0
while True:
    k += 1
    s += k
    if s >= n:
        break
print(k-1)