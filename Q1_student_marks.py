from functools import reduce

marks = [45, 67, 32, 50, 89]

# a) Filter students scoring 50 or above
passed = list(filter(lambda x: x >= 50, marks))

# b) Add 5 grace marks, maximum 100
updated = list(map(lambda x: min(x + 5, 100), marks))

# c) Calculate total marks
total = reduce(lambda x, y: x + y, updated)

print("Passed marks:", passed)
print("Updated marks:", updated)
print("Total marks:", total)
