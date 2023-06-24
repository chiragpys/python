square_dict = dict()
for num in range(1, 6):
    square_dict[num] = num*num
print(square_dict, "\n")

# dictionary comprehension example
square_dict = {num: num*num for num in range(1, 6)}
print(square_dict, "\n")


original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
even_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0}
print(even_dict)


