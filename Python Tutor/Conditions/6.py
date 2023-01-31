a = int(input())
b = int(input())
c = int(input())

if a == b and a == c and b == c:
    print(3)
elif (a == b and a != c and b != c) or (b == c and b != a and c != a) or (a == c and a != b and c != b):
    print(2)
else:
    print(0)