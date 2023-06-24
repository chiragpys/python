# You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
# For example, alison heck should be capitalised correctly as Alison Heck.

# Sample Input
# chris alan

# output
# Chris Alan

def solve(s):
    s = s.split(" ")
    for i in range(0, len(s)):
        s[i] = s[i].capitalize()
    p = " ".join(s)
    return p


s = input("Enter your name:")
result = solve(s)
print(result)
