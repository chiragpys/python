# Task The provided code stub reads and integer,n , from STDIN. For all non-negative integers i<n, print i2.


# Example
# n = 3
# The list of non-negative integers that are less than n =3  is[0, 1, 2]. Print the square of each number on a
# separate line.

# Output
# 0
# 1
# 4

n = int(input("Enter a number: "))

for i in range(n):
    print(i * i)

