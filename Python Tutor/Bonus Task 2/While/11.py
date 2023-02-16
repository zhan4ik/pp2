n = int(input())
s = 0
while n != 0:
    m = int(input())
    if m != 0 and n < m:
        s += 1
    n = m
print(s)