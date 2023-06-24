def addition(n):
    return n * n


numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# lambda
numbers = (1, 2, 3, 4)
result = map(lambda x: x*x*x, numbers)
print(list(result))

# Add two lists using map and lambda

numbers1 = [1, 2, 3, 4, 5, 6]
numbers2 = [4, 5, 6, 8, 9, ]
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))


l = ['sat', 'bat', 'cat', 'mat', 'rat']
test = list(map(list, l))
print(test)

n = 12345
test = list(map(int, str(n)))
print(sum(test))



def even(num):
    if num % 2 == 0:
        return num * num * num
    else:
        return num


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(map(even, numbers))
print(result)

n = [4, 3, 2, 1]
print(list(map(lambda x: x*2, n)))
