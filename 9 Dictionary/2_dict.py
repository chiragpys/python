# add item
numbers = {1: "One", 2: "Two", 3: "Three"}
print(numbers)
numbers[4] = "Four"
print(numbers,"\n")

# Change Value
Id = {111: "python", 112: "C++", 113: "django"}
print("Initial Dictionary: ", Id)
Id[112] = "Pandas"
print("Updated Dictionary: ", Id, "\n")

# Remove item
Id = {111: "python", 112: "C++", 113: "django"}
print("Initial Dictionary: ", Id)
del Id[111]
print("Updated Dictionary: ", Id, "\n")


squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

print(1 in squares)
print(2 not in squares)
print(49 in squares, "\n")

# Iterating
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i], end=" ")
print()

# Keys
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares.keys():
    print(i, end=" ")
print()

# values
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares.values():
    print(i, end=" ")
print()

# Items
print("\n")
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i, j in squares.items():
    print(i, j)

