n = int(input('N = '))

def mygenerator(n):
    for i in range(0, n):
        if (i % 2 == 1):
            yield i

mylist = []
for val in mygenerator(n):
    mylist.append(str(val))


print(', '.join(mylist))
