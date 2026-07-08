#WAP to input a number (3-digit or more). Arrange the digits of the number in ascending order and display the result.
def sortdig(num, lis):
    if num == 0:
        lis.sort()
        return lis

    
    lis.append(num % 10)
    return sortdig(num // 10, lis)



A = int(input("Enter a number: "))
print("The digits in order are:")
for e in sortdig(A,[]):
    print(e,end='')