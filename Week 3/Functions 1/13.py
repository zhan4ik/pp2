import random

name = str(input("Hello! What is your name?\n"))
ans = random.randint(1, 5)
k = 0
n = 0
print("\nWell, " + name + ", I am thinking of a number between 1 and 20.")

while n != ans:
    n = int(input("\nTake a guess.\n"))
    k += 1
    if n != ans:
        print("Your guess is too low.\nTake a guess.\n")
    else: 
        print(f"Good job, " + name + "! You guessed my number in " + str(k) + " guesses!")

