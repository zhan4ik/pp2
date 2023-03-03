fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)