def checkunique(n,d=None):
    d1=n%10
    if d == d1:
        return False
    elif n>0:
        checkunique(n//10,d)
    else:
        return True
    
def isunique(n):
    d=n%10
    if n>9:
        if checkunique(d,n//10)==False:
            return False
        else:
            isunique(n//10)
    else:
        return True       
        
num=int(input("Enter the number you want to check: "))
if isunique(num):
    print("Your number is unique.")
else:
    print("Your number is not unique.")