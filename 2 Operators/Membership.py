a = [1, 2, 3, 4, 5, 6, 7]
b = [2, 4, 6, 8, 10]

for i in a:
    if i in b:
        print("Overlapping", i)
    else:
        print("Not overlapping")