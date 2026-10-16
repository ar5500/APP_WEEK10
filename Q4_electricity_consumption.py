from functools import reduce

consumption = [8, 12, 9, 15, 11]

high = list(filter(lambda x: x > 10, consumption))
cost = list(map(lambda x: x * 6, consumption))
total = reduce(lambda x, y: x + y, consumption)

def calculate_bill(units):
    return units * 6

print("High consumption:", high)
print("Daily costs:", cost)
print("Total consumption:", total)
print("Total bill:", calculate_bill(total))
