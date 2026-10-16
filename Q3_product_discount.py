prices = [500, 1200, 2500, 900, 1500]

def discount(price):
    return price * 0.80 if price > 1000 else price
new_prices = list(map(discount, prices))

eligible = list(filter(lambda p: p > 1000, prices))

print("Original prices:", prices)
print("Eligible products:", eligible)
print("Discounted prices:", new_prices)
