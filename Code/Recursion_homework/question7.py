#WAP to input a number and check whether the number is unique or not

def is_unique(num,lis):
    if num == 0:
        return True
    
    currentdig=num%10

    if currentdig in lis:
        return False
    else:
        lis.append(currentdig)

    return is_unique(num//10,lis)


num=int(input("Enter the number you want to check: "))

f=is_unique(num,[])

if f==True:
    print("The number you wanted to check is a unique number.")
else:
    print("The number you wanted to check is not a unique number.")
