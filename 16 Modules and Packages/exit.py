import sys

age = int(sys.argv[1])

if age < 18:

    # exits the program
    sys.exit("Age less than 18")
else:
    print("Age is not less than 18")
