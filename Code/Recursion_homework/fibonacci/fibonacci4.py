def fibonacci(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def in_fib(num: int):
    n = 0
    while True:
        val = fibonacci(n)
        if val == num:
            return True
        elif val > num:
            return False
        n += 1


num=int(input("Enter the numberr you want to check:"))
if in_fib(num):
    print("Your number is in the Fibonacci sequence.")
else:
    print("Your number is n't in the Fibonacci sequence.")