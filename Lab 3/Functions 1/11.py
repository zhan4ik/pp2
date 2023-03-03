s = str(input())

def isPalindrome(string):
    s1 = s[:len(s) // 2]
    s2 = s[(len(s) + 1) // 2:]
    if s1 == s2[::-1]:
        print(s + " is a palindrome")
    else:
        print(s + " is not a palindrome")

isPalindrome(s)
