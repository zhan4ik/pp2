n = int(input('N = '))

def mygen(n):
    for i in range(n):
        if (i % 3 == 0 and i % 4 == 0):
            yield i

mylist = []
for val in mygen(n):
    mylist.append(str(val))

print(', '.join(mylist))
