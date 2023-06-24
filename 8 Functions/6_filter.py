def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if variable in letters:
        return True
    else:
        return False


sequence = ['g', 'o', 'o', 'g', 'l', 'e']
filtered = filter(fun, sequence)
print(list(filtered))

seq = [0, 1, 2, 3, 5, 8, 13, 10]
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))

result = filter(lambda x: x % 2 == 0, seq)
print(list(result))


def even(num):
    if num % 2 == 0:
        return True


n = list(range(1, 10))
result = filter(lambda x: even(x), n)
print(list(result))




