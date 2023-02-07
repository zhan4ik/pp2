n = int(input())
s = 0
m = 1

for i in range(1, n+1):
    m *= i
    s += m
    
print(s)