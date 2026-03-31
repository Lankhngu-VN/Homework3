n = int(input())
chan = 0
le = 0
for i in range(1, n+1):
    if i%2 == 0:
        chan +=1
    else:
        le +=1
print(f'so so chan: {chan}')
print(f'so so le: {le}')