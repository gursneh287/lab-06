
N = int(input("enter a number:"))
sum = 1
i = 1
while i <= N:
    sum = sum + (1/(1+i))
    i += 1
print(sum)
