n = int(input())
s=0
a=n
while a>0:
    b=a%10
    s+=b
    a=a//10
print(s)