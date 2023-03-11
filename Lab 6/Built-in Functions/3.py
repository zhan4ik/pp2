s = str(input())
sr = s[::-1]
if s == sr:
    print(f"{s} is palindrome")
else:
    print(f"{s} is not palindrome")