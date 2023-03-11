import os
f = r"C:\Users\sicpa\OneDrive\Рабочий стол\KBTU\Semester 2\Programming Principles II\Lab 6\sample.txt"

with open(f, 'r') as file:
    x = len(file.readlines())
    print("lines:", x)