thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
thislist.insert(1, "orange")

tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)

thistuple = ("kiwi", "orange")
thislist.extend(thistuple)

print(thislist)