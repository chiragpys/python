# set method

# add method
numbers = {21, 34, 54, 12}
print('Initial Set:', numbers)
numbers.add(32)
print('Updated Set:', numbers,"\n")


# Update
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']
companies.update(tech_companies)
print(companies, "\n")


# Removes to discard()
languages = {'Swift', 'Java', 'Python'}
print('Initial Set:', languages)

removedValue = languages.discard('Java')
print('Set after remove():', languages, "\n")

# len
even_numbers = {2, 4, 6, 8}
print('Set:', even_numbers)
print('Total Elements:', len(even_numbers))
print(even_numbers.pop())

