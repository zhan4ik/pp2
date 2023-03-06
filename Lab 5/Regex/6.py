import re
a = '''
sdjfjak,ajsdjf.jskajaf,akdf.
'''
x = re.sub('[ .,]', ':', a)
print(x)
