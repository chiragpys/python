# Let's learn about list comprehensions! You are given three integers x, y and z representing the dimensions of a
# cuboid along with an integer n . Print a list of all possible coordinates given by(i,j,k)  on a 3D grid where the
# sum i+j+k of  is not equal to n. Here,0<i<x;0<j<y;0<k<z. Please use list comprehensions rather than multiple loops,
# as a learning exercise.

# Example:
# 1
# 1
# 1
# 2

# output
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

x = int(input("Enter a number for x:"))
y = int(input("Enter a number for y:"))
z = int(input("Enter a number for z:"))
n = int(input("Enter a number for n:"))
l = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
print(l)


# without list comprehensions
# a = []
# for i in range(x + 1):
#     for j in range(y + 1):
#         for k in range(z + 1):
#             if i+j+k !=0:
#                 a.append([i,j,k])
# print(a)