from functools import reduce

salaries = [35000, 42000, 28000, 50000, 39000]
revised = list(map(
    lambda s: s * 1.10 if s < 40000 else s,
    salaries
))
eligible = list(filter(lambda s: s < 40000, salaries))

total = reduce(lambda x, y: x + y, revised)

print("Eligible salaries:", eligible)
print("Revised salaries:", revised)
print("Total expenditure:", total)
