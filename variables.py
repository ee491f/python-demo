print("hi from file")

numberVariable = 3.3
print(numberVariable)

stringVariable = "hi from string"
print(stringVariable)

# lists do allow duplicates
listVariable = [
  1,
  "two",
  1,
]
print(listVariable)
print(listVariable[1])

# sets do not allow duplicates
setVariable = set([
  1,
  "two",
  1,
])
print(setVariable)
print("three" in setVariable)

dictVariable = {
  "key": "value",
  stringVariable: "value2",
  "key3": stringVariable,
}
print(dictVariable)
print(dictVariable['key'])