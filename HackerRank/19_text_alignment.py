# You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
# Your task is to replace the blank (______) with rjust, ljust or center.

n = int(input("Enter a number:"))
value = n * 2 - 1
value2 = int((n + 1) / 2)

for i in range(0, n):
    character = 'H' * (i * 2 + 1)
    print(character.center(value, " "))

name = 'H' * n

for i in range(1, n + 2):
    print(name.center(value, " ") + name.rjust(int((9 * n - value) / 2), " "))

for i in range(1, value2 + 1):
    name1 = 'H' * (5 * n)
    print(name1.center(6 * n - 1, " "))

for i in range(1, n + 2):
    print(name.center(value, " ") + name.rjust(int((9 * n - value) / 2), " "))

b = value
for i in range(b, 0, -2):
    name2 = 'H' * i
    print(" " * (4 * n) + name2.center(value, " "))