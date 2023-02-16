max = 0
a = -1
i = -1
imax = 0
while a != 0:
    a = int(input())
    i += 1
    if a > max:
        max = a
        imax = i        
print(imax) 