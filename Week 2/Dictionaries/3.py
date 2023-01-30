thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
thisdict.pop("model")
thisdict.popitem()
print(thisdict)

for x, y in thisdict.items():
  print(x, y)