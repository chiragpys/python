# You are given the firstname and lastname of a person on two different lines.
# Your task is to read them and print the following:

# Hello firstname lastname! You just delved into python.

def print_full_name(first, last):
    return print(f"Hello {first.capitalize()} {last.capitalize()}! You just delved into python.")


first_name = input("Enter a First name: ")
last_name = input("Enter a last name: ")
print_full_name(first_name, last_name)

