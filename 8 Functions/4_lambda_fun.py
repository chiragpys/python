x = lambda a: a+10
print(x(5))

str1 = 'Python'

rev_upper = lambda string: string.upper()[::-1]
print(rev_upper(str1))


Max = lambda a, b : a if(a > b) else b
print(Max(1, 2))

lis1 = ["Python", "asw", "C", "C++", "Django", "MySQL", "Pandas"]

lis1.sort(key=lambda x: len(x))
print(lis1)







