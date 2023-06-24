# String method
print("capitalize")
str1 = 'python'
str2 = str1.capitalize()
print("Old value:", str1)
print("New value:", str2, "\n")

print("casefold")
str1 = 'PYTHON'
str2 = str1.casefold()
print("Old value:", str1)
print("New value:", str2, "\n")

print("upper")
str1 = 'PyThon'
str2 = str1.upper()
print("Old value:", str1)
print("New value:", str2, "\n")

print("lower")
str1 = 'PyThon'
str2 = str1.lower()
print("Old value:", str1)
print("New value:", str2, "\n")

print("title")
str1 = 'PyThon proGramming'
str2 = str1.title()
print("Old value:", str1)
print("New value:", str2, "\n")

print("count")
str1 = 'PyThon proGramming'
str2 = str1.count('n')
print("occurances:", str2, "\n")

print("replace")
str1 = 'Python Programming'
str2 = str1.replace('Programming', 'is easy')
print(str2, "\n")

print("split")
str1 = 'Python Programming is easy to learn'
str2 = str1.split()
print(str1)
print(str2, "\n")

print("center")
mystring = "Hello"
x = mystring.center(12, "-")
print(x,"\n")

print("count")
mystr = "Hello Python"
print(mystr.count("l"),"\n")

print("find")
mystring = "Python"
print(mystring.find("P"))
print(mystring.find("on"),"\n")

print("index")
mystring = "HelloPython"
print(mystring.index("P"))
print(mystring.index("hon"),"\n")

print("isalnum")
mystring = "HelloPython"
print(mystring.isalnum())
a = "123"
print(a.isalnum())
a = "@#$%^"
print(a.isalnum(),"\n")

print("isalpha")
mystring = "HelloPython"
print(mystring.isalpha())
a = "123"
print(a.isalpha(),"\n")

print("isdecimal")
mystring = "HelloPython"
print(mystring.isdecimal())
a = "1.23"
print(a.isdecimal())
a = "123"
print(a.isdecimal(),"\n")

print("islower")
mystring = "HelloPython"
print(mystring.islower())
a = "python_3.10"
print(a.islower(),"\n")

print("isnumeric")
c = "123"
print(c.isnumeric())
c = "Python_3.10"
print(c.isnumeric(),"\n")

print("isprintable")
c = "123"
print(c.isprintable())
c = "\t"
print(c.isprintable(),"\n")

print("join")
a = "-"
print(a.join("123"))

print("strip")
a = "    Hello Python "
print(a.strip(),"\n")

print("chr to <str>")
print(chr(78))
print("ord to <int>")
print(ord("N"))


