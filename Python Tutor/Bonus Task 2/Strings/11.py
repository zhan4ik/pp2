s = str(input())

for i in range(len(s) + 1):
    if i // 3 != 0:
        print(s[i], end="")