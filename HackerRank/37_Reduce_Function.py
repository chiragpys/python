# Given a list of rational numbers,find their product.

# Output
# Format Print only one line containing the numerator and denominator of the product of the numbers in the
# list in its simplest form, i.e. numerator and denominator have no common divisor other than 1.

# Sample input
# 3
# 1 2
# 3 4
# 10 6

# Sample output
# 5 8

from fractions import Fraction
from functools import reduce


def product(fracs):
    t = Fraction(reduce(lambda x, y: x * y, fracs))
    return t.numerator, t.denominator


fracs = []
for _ in range(int(input("Enter a number: "))):
    fracs.append(Fraction(*map(int, input().split())))
result = product(fracs)
print(*result)




