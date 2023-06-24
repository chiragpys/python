# Function Arguments

# x is even or odd
def EvenOdd(x):
    if x % 2 == 0:
        print("even")
    else:
        print("odd")


EvenOdd(2)
EvenOdd(3)
print()


# default argument
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)


myFun(10)
myFun(10, 40)
print()


# Keyword Arguments
def student(firstname, lastname):
    print(firstname, lastname)


student(firstname='Python', lastname='Practice')
student(lastname='Django', firstname='Practice')
print()


# Positional Arguments
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)


print("Case-1:")
nameAge("Pyhon", 3.10)

print("\nCase-2:")
nameAge(3.10, "Python")
print()


# Variable length non-keywords argument
def myFun(*args):
    for arg in args:
        print(arg)


myFun('Hello', 'Welcome', 'to', 'Python')
print()


# Variable length keyword arguments
def myFun(**kwargs):
    for key, value in kwargs.items():
        print(key, "-", value)


myFun(first='Welcome', mid='to', last='Python')
print()


# Docstring
def evenOdd(x):
    """Function to check if the number is even or odd"""

    if x % 2 == 0:
        print("even")
    else:
        print("odd")


print(evenOdd.__doc__)
print()


# return statement
def square_value(num):
    """This function returns the square value of the entered number"""
    return num ** 2


print(square_value(2))
print(square_value(-4))

