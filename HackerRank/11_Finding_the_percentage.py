# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
# Print the average of the marks array for the student name provided, showing 2 places after the decimal.

"""
Example
marks key: value pair are
'alpha': [20,30,40],
'beta': [30,50,70]
query_name = 'beta'
The query_name is 'beta'. beta's average score is(30+50+70)/3 = 50.0.
"""

n = int(input("Enter a number: "))
student_marks = {}

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input("Enter a query name: ")

for i, j in student_marks.items():
    if i == query_name:
        a = float(sum(j) / 3)
        print("%.2f" % a)
