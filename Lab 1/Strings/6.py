age = 36
txt = "My name is John, I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


myorder = "I want {2} pieces of item {0} for {1} dollars."
print(myorder.format(quantity, itemno, price))