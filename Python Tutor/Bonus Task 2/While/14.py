fib1 = 1
fib2 = 1
n = int(input())
i = 0
if n==0:
    print(0)
else:
    while i < n - 2:
        sum = fib1 + fib2
        fib1 = fib2
        fib2 = sum
        i = i + 1
    print(fib2)