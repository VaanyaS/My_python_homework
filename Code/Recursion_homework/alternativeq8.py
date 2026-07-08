def sortdig(num, lis):
    if num == 0:
        lis.sort()
        f=''.join(map(str,lis))
        return f

    
    lis.append(num % 10)
    return sortdig(num // 10, lis)



A = int(input("Enter a number: "))
print("The digits in order are:", sortdig(A,[]))
