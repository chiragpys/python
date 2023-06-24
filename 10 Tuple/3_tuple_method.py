# tuple method

# 1.count

Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2, 3)
Tuple2 = ('python', 'geek', 'python', 'for', 'java', 'python')
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)

res = Tuple2.count('python')
print('Count of Python in Tuple2 is:', res)


Tuple = (0, 1, (2, 3), (2, 3), 1, [3, 2], 'geeks', (0,))
res = Tuple.count((2, 3))
print('Count of (2, 3) in Tuple is:', res)

res = Tuple.count([3, 2])
print('Count of [3, 2] in Tuple is:', res, "\n")

# 2.index
Tuple = (0, 1, 2, 2, 3, 1, 3, 2)

res = Tuple.index(3)
print('First occurrence of 3 is', res, "\n")

languages = ('Python', 'Swift', 'C++')
for i in languages:
    print(i)

languages = ('Python', 'Swift', 'C++')
print('C' in languages)
print('Python' in languages)


