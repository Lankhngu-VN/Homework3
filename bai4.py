h = int(input())
for i in range(1, h+1):
    if i  == 1:
        print(" "*(h-1) + "*")
    elif i == h:
        print("*"*(2*h-1))
    else:
        print(" "*(h-i) + "*" + " "*(2*i-3) + "*")