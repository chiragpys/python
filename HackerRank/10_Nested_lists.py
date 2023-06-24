# Given the names and grades for each student in a class of N students, store them in a nested list and print the
# name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each
# name on a new line.

# Explanation There are 5 students in this class whose names and grades are assembled to build the following list:
# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]] The lowest
# 37.2 grade of  belongs to Tina. The second lowest grade of 37.21  belongs to both Harry and Berry, so we order
# their names alphabetically and print each name on a new line.

Result = []
scorelist = []

for _ in range(int(input("Enter a number:"))):
    name = input("Enter a name:")
    score = float(input("Enter a score:"))
    Result += [[name, score]]
    scorelist += [score]
b = sorted(list(set(scorelist)))[1]

for a, c in sorted(Result):
    if c == b:
        print(a)
