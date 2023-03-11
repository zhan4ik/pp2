import os
f = r"C:\Users\sicpa\OneDrive\Рабочий стол\KBTU\Semester 2\Programming Principles II\Lab 6"

print('existence:', os.access(f, os.F_OK))
print('readability:', os.access(f, os.R_OK))
print('writability:', os.access(f, os.W_OK))
print('executability:', os.access(f, os.X_OK))