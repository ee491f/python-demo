numberVariable = 3.3
listVariable = [
  1,
  "two",
  1,
]
dictVariable = {
  "key1": "value1",
  "key2": "value2",
  "key3": "value3",
}

if numberVariable >= 3:
  print("greater or equal")
else:
  print("lesser")

print("===printing list===")
for listItems in listVariable:
  print(listItems)
else:
  print("hi from else")
print("===printing list with index===")
for index, listItems in enumerate(listVariable):
  print(str(index) + "(index): " + str(listItems) + "(element)")
else:
  print("hi from else")

print("===printing dictionary===")
for dictValue in dictVariable:
  print(dictValue)
  # print(dictVariable[dictValue])

print("===printing dictionary with key===")
for dictKey, dictValue in dictVariable.items():
  print(str(dictKey) + "(key): " + str(dictValue) + "(value)")
