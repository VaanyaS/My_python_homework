# WAP to input a number and count number of digits present in it using recursion:
 
def countDigit(num):
    if num == 0:
        return 0
    else:
        return 1+countDigit(num//10)
 
#main code
N = int(input('Enter any positive integer value:'))
C = countDigit(N)
print(f'Number of digits is: {C}')
 
# Output:
# Enter any positive integer value: 346
# Number of digits is: 3
 