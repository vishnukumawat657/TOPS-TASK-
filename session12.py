#1

gst_price = lambda price: price + (price * 0.18)

print(gst_price(100))
print(gst_price(250))
print(gst_price(500))

# 2
songs = [' shape OF you ', '  believer', 'BLINDING lights  ', ' kesariya ']

clean_songs = list(map(lambda song: song.strip().title(), songs))

print(clean_songs)


# 3

products = ["Shoes", "Shirt", "Mobile", "Sofa", "Laptop"]

result = list(filter(lambda product: product.lower().startswith("s"), products))

print(result)

# 4

from functools import reduce

orders = [120, 340, 560, 80]

total = reduce(lambda x, y: x + y, orders)

print("Total Bill:", total)

# 5
from functools import reduce

numbers = [40, 60, 80, 120]

doubled = list(map(lambda x: x * 2, numbers))

filtered = list(filter(lambda x: x > 100, doubled))

total = reduce(lambda x, y: x + y, filtered)

print("Doubled:", doubled)
print("Filtered:", filtered)
print("Total:", total)

