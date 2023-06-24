# Task Apply your knowledge of the .add() operation to help your friend Rupal. Rupal has a huge collection of country
# stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your
# help. You pick the stamps one by one from a stack of N country stamps.
# Find the total number of distinct country stamps.

# sample input
# 7
# UK
# China
# USA
# France
# New Zealand
# UK
# France

# sample output
# 5

# Explanation
# UK and France repeat twice. Hence, the total number of distinct country stamps is  (five).

N = int(input())
a = [input() for _ in range(N)]
a = set(a)
count = 0
for j in range(len(a)):
    count += 1
print(count)

