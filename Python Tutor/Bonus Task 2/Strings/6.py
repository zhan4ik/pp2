s = str(input())
cnt = 0

for i in range(len(s)):
    if s[i] == 'f':
        cnt += 1
        if cnt == 2:
            print(i)
    