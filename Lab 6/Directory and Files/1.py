import os

f = r"C:\Users\sicpa\OneDrive\Рабочий стол\KBTU\Semester 2\Programming Principles II\Lab 6"
print([name for name in os.listdir(f)])
print([name for name in os.listdir(f) if os.path.isdir(os.path.join(f, name))])
print([name for name in os.listdir(f) if not os.path.isdir(os.path.join(f, name))])