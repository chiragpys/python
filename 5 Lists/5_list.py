# List method

# append()
a = ['Mathematics', 'chemistry', 2000, 2001]
print(a)

# extend()
List1 = [1, 2, 3]
List2 = [4, 5]
List1.extend(List2)
print(List1)

# insert()
a.insert(2,"python")
print(a)

# remove()
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
List.remove(3)
print(List)

# pop()
# print(List.pop())

# clear
List1 = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
List1.clear()
print(List1)

# index()
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.index(2))

# count()
print(List.count(1))

# sort()
List = ['q', 'r', 'g', 'c', 's', 'o', 'a', 'k']
List.sort()
print(List)

# reverse()
List.sort(reverse=True)
print(List)

# min()
numbers = [5, 2, 8, 1, 9]
print(min(numbers))

# max()
numbers = [5, 2, 8, 1, 9]
print(max(numbers))

# sum()
numbers = [5, 2, 8, 1, 9]
print(sum(numbers))

# len()
numbers = [5, 2, 8, 1, 9]
print(len(numbers))
