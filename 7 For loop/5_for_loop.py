# continue & break
for i in range(10):
    if i == 5:
        continue
    elif i == 8:
        break
    else:
        print(i)
# pass
print("\npass Statement ")
for letter in 'Python':
    pass
print('Last Letter :', letter)

# loop else
print("\nLoop else")
for i in range(5):
    print(i)
else:
    print("No break")
