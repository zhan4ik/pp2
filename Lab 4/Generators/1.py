n = int(input('N = '))

def mygenerator(n):
    for i in range(1, n):
        yield i*i

for val in mygenerator(n):
    print(val)
