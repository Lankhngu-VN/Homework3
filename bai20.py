n = input()
count = 0
prime = { "2" , "3" , "5" , "7" }
for i in n:
    if i in prime:
        count += 1
print(count)
