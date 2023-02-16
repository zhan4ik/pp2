n = int(input())
two = 2
power = 1
while two <= n:
    two *= 2
    power += 1
print(power - 1, two // 2)
