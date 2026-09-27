# 1

product = "Redmi Note 12 Pro"

print(product.upper())
print(product.lower())


# 2

def clean_brand_name(name):
    name = name.strip()
    name = name.replace("-", " ")
    return name

print(clean_brand_name(" oneplus-Nord "))


# 3

product = "Apple iPhone 14 Pro Max"

words = product.split()

brand = product[:5]
model = product[6:]

print("Brand:", brand)
print("Model:", model)

# 4

def format_product_display(name, price):
    return name + " - ₹" + str(price)

print(format_product_display("Boat Earbuds", 1299))

# 5

products = [' mi-Band 5 ', ' SAMSUNG-Galaxy ', ' realme-Book ']

cleaned = []

for product in products:
    product = product.strip()
    product = product.replace("-", " ")
    product = product.title()
    cleaned.append(product)

print(cleaned)