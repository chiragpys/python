dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}

# copy() method
print("copy method")
dict2 = dict1.copy()
print(dict2, "\n")

# clear() method
print("clear method")
dict1.clear()
print(dict1, "\n")

# get() method
print("get method")
print(dict2.get(1), "\n")

# items() method
print("item method")
print(dict2.items(), "\n")

# keys() method
print("key method")
print(dict2.keys(), "\n")

# pop() method
print("pop method")
dict2.pop(4)
print(dict2, "\n")

# popitem() method
print("popitem method")
dict2.popitem()
print(dict2, "\n")

# update() method
print("update method")
dict2.update({3: "Scala"})
print(dict2, "\n")

# values() method
print("values method")
print(dict2.values())

