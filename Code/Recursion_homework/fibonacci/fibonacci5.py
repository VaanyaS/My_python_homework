m=0
lis=[]
def fibonacci(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

length=int(input("Enter the maximum amout of numbers you want to see:"))
while m <= length:
    val=fibonacci(m)
    if val%2==0:
        lis.append(val)
        m+=1
    else:
        m+=1
        continue

print(lis)