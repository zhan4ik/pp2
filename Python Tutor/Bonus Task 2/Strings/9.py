s = str(input())

for i in range(len(s)):
    if s[i] == 1:
        print(s.replace(s[i], 'one'))
