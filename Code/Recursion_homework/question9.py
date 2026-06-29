#WAP to display if a numbar is composite or not using recursion

def composit(num,div):
    if num<=3:
        return False
    
    if div==num:
        return False

    if num % div==0:
        return True
    
    else:
        return composit(num,div+1)
    

num=int(input("Enter the number you want to check (It should be between 1 and 100)"))

if 1>num or num >100:
    print("Please inpt a number between 1 and 100.")
else:
    f=composit(num,2)

if f==True:
    print("Your number is composite!")
if f==False:
    print("Your number is not composite.")