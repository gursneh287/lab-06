x = float(input("enter value of x:"))
N = float(input("enter number of terms:"))
sum = 1
i = 1
while i<=N:
    sum = sum + ((x**i)/(i))
    i+=1
print(sum)