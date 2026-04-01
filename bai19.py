A = int(input())
n1= 1
n2= 2
while n2 < A:
    n3 = n1 + n2
    n1 = n2 
    n2 = n3
print(n1)