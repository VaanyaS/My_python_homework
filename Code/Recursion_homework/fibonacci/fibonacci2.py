n=0
def fibonacci(n:int):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
while True==True:
    val=fibonacci(n)
    if val>1000:
        break
    if 100 <= val <= 1000:
        print(val)
        n+=1

