import math
r = int(input())

def volumeOfSphere(r):
    v = (4 * math.pi * r**3) / 3
    print('%.2f'%v)
    
volumeOfSphere(r)
    