import os
f = r"C:\Users\sicpa\OneDrive\Рабочий стол\KBTU\Semester 2\Programming Principles II\Lab 6"

if os.access(f, os.F_OK):
    print([name for name in os.listdir(f)])