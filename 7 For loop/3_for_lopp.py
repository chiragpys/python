# Iterating over a list
print("List Iteration")
l = ['Swift', 'Python', 'Go', 'JavaScript']
for i in l:
    print(i)

# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ('Swift', 'Python', 'Go', 'JavaScript')
for i in t:
    print(i)

# Iterating over a String
print("\nString Iteration")
s = "Python"
for i in s:
    print(i)

# Iterating over dictionary
print("\nDictionary Iteration")
d = {'a': 123, 'b': 345}
for i, j in d.items():
    print(i, j)

# Iterating over a set
print("\nSet Iteration")
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i)
