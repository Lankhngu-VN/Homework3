a = int(input())
Tong_uoc=0
for i in range(1, a):
    if a%i==0:
        Tong_uoc+=i
if Tong_uoc==a and a>1:
    print("a la so hoan hao")
else:
    print("a khong la so hoan hao")