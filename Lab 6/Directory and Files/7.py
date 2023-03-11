with open('Lab 6\lol1.txt', 'r') as file1, open('Lab\lol2.txt', 'a') as file2:
    for line in file1:
        file2.write(line)