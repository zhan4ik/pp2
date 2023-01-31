n = int(input())
str1 = "The next number for the number {0} is {1}."
str2 = "The previous number for the number {0} is {1}."

print(str1.format(n, n + 1))
print(str2.format(n, n - 1))