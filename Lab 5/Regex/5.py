import re
a = '''
aaldkgsb
'''
x = re.findall(r".*a.*b$", a)
print(x)
