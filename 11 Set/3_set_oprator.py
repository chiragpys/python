# set operators

# union()

A = {1, 3, 5}
B = {0, 2, 4}

print('Union using |:', A | B)
print('Union using union():', A.union(B), "\n")

# intersection
A = {1, 3, 5}
B = {1, 2, 3}

print('Intersection using &:', A & B)
print('Intersection using intersection():', A.intersection(B), "\n")

# difference
A = {2, 3, 5}
B = {1, 2, 6}

print('Difference using &:', A - B)
print('Difference using difference():', A.difference(B), "\n")

# symmetric
A = {2, 3, 5}
B = {1, 2, 6}
print('using ^:', A ^ B)
print('using symmetric_difference():', A.symmetric_difference(B), "\n")


# Check two set are equal
A = {1, 3, 5}
B = {3, 5, 1}
if A == B:
    print('Set A and Set B are equal')
else:
    print('Set A and Set B are not equal')
