import re
a = '''
a
aaa
Idjs
Aaafs
'''
x = re.findall('[A-Z]+[a-z]+', a)
print(x)
