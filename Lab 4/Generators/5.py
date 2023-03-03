def gen_print():
    mylist = []
    for val in mygen(n):
        mylist.append(str(val))
    print(', '.join(mylist))


n = int(input('N = '))


def mygen(n):
    for i in range(n, -1, -1):
        yield i


gen_print()
