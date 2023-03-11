import math, time

x = int(input())
m = int(input())
time.sleep(m / 1000)

a = math.sqrt(x)

print(f"Square root of {x} after {m} miliseconds is {a}")