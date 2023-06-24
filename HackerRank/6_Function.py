# Task
# Given a year, determine whether it is a leap year.
# If it is a leap year, return the Boolean True, otherwise return False.
# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function.
# It is only necessary to complete the is_leap function.

# Example:
# 1990
# False
# 1990 is not a multiple of 4 hence it's not a leap year.

def is_leap(year):
    leap = False
    if (year % 400 == 0) and (year % 100 == 0):
        return True
    elif (year % 4 == 0) and (year % 100 != 0):
        return True
    return leap


year = int(input("Enter a year you have to check leap year: "))
print(is_leap(year))


