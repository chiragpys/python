import copy

li1 = [1, 2, [3, 5], 4]
li2 = li1.copy()
print("li1 ID: ", id(li1), "Value: ", li1)
print("li2 ID: ", id(li2), "Value: ", li2)

li3 = copy.copy(li1)
print("li3 ID: ", id(li3), "Value: ", li3)

li4 = copy.deepcopy(li1)
print("li3 ID: ", id(li4), "Value: ", li4)

li2[2][0] = 4
print(li1)
print(li4)

