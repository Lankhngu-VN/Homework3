n = int(input())
dem = 1
s = n//10
while True:
    s = s//10
    dem +=1
    if s <=1:
        break
print(dem+1)