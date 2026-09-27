# 1
def calculate_final_price(price, discount_rate):
    discount = price * discount_rate
    final_price = price - discount
    return final_price

result = calculate_final_price(1200, 0.15)

print("Final Price:", result)

# 2
def get_delivery_charge(amount, city="Ahmedabad"):
    if city == "Ahmedabad":
        return 30
    else:
        return 50

print(get_delivery_charge(500))
print(get_delivery_charge(500, "Mumbai"))


#  3

def format_coupon_message(username, discount=10):
    return f"Hi {username}, you get {discount}% off!"

print(format_coupon_message("Rahul", 20))
print(format_coupon_message("Amit"))

# 4

def apply_discount(price, rate=0.10):
    discount = price * rate
    final_price = price - discount
    return final_price

result = apply_discount(1000)

print("Final Price:", result)

# 5

def calculate_cashback(amount, cashback_rate=0.05):
    cashback = amount * cashback_rate
    return cashback


zomato_cashback = calculate_cashback(500)
print("Zomato Cashback:", zomato_cashback)


flipkart_cashback = calculate_cashback(2000, 0.07)
print("Flipkart Cashback:", flipkart_cashback)