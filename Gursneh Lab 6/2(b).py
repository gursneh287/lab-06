N = int(input("enter a number:"))
sum = 0
i = 1
while i<=N:
    fact = 1
    j = 1
    while j<=i: 
        fact = fact * j
        j+=1
    sum = sum+(1/fact)
    i += 1
print(sum)