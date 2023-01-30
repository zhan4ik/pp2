car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
car["color"] = "white"
print(x)

y = car.values()
car["year"] = 2020
print(y)

z = car.items()
print(z) 

if "model" in car:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")