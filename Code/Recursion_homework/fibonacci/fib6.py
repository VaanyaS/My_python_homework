lis=[]
v=0
def fibonacci(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

length=int(input("Enter the maximum amout of numbers you want to use:"))

while v <= length:
    val=fibonacci(v)
    lis.append(val)
    v+=1

print("Here are the values:", lis)
print(f"The sum of the values is: {sum(lis)}")