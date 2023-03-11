import os

f = r'C:\Users\sicpa\OneDrive\Рабочий стол\KBTU\Semester 2\Programming Principles II\Lab 6\text.txt'
ok = os.access(f, os.F_OK)
if not ok:
    print('Does not exist')
elif ok:
    os.remove(f)
    print("Removed")