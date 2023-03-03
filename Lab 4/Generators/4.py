def gen_print():
    lmylist = []
    for val in squares(n):
        mylist.append(str(val))
    print(', '.join(mylist))


n = int(input('a = '))
b = int(input('b = '))


def squares(n):
    for i in range(n, b):
        yield i*i


gen_print()
