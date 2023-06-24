# You are given an integer N followed by N email addresses. Your task is to print a list containing only valid email
# addresses in lexicographical order.

# Valid email addresses must follow these rules:
# It must have the username@websitename.extension format type.
# The username can only contain letters, digits, dashes and underscores.
# [a-z], [A-Z],[0-9],[-].
# The website name can only have letters and digits [a-z], [A-Z],[0-9].
# The extension can only contain letters [a-z], [A-Z].
# The maximum length of the extension is 3.

# Sample input
# 3
# lara@hackerrank.com
# brian-23@hackerrank.com
# britts_54@hackerrank.com

# Sample output
# ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']


import re


def fun(s):
    regex = r"^([a-zA-Z0-9-_]+)@([a-zA-Z0-9]+)\.([a-zA-Z]{,3})$"
    if re.fullmatch(regex, s):
        return bool


def filter_mail(emails):
    return list(filter(fun, emails))


n = int(input("Enter a number: "))
emails = []
for _ in range(n):
    emails.append(input("Enter a email: "))

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)


