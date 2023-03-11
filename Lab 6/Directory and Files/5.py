import os

f = r"C:\Users\sicpa\OneDrive\Рабочий стол\KBTU\Semester 2\Programming Principles II\Lab 6\sample.txt"
mylist = ["Manchester City >> Liverpool", "Ronaldo >> Messi"]

with open(f, "w") as file:
    for x in mylist:
        file.write(x + '\n')