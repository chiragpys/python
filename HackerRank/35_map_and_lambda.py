# Let's learn some new Python concepts! You have to generate a list of the first N fibonacci numbers, 0 being the first
# number. Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.

# Output Format
# A list on a single line containing the cubes of the first N fibonacci numbers.

# Sample input
# 5

# Sample output
# [0, 1, 1, 8, 27]

# Explanation
# The first 5 fibonacci numbers are[0,1,1,2,3], and their cubes are[0,1,1,8,27].


cube = lambda x: x ** 3

lst = []


def fibonacci(n):
    x = 0
    y = 1
    for i in range(n):
        nxt = x + y
        lst.append(x)
        x = y
        y = nxt
    return lst


n = int(input("Enter a number: "))
print(list(map(cube, fibonacci(n))))


