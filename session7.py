# 1

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible for IPL ticket booking")
else:
    print("Not eligible")

# 2
followers = int(input("Enter number of followers: "))

if followers < 10000:
    print("Micro Influencer")
elif followers <= 100000:
    print("Rising Star")
else:
    print("Celebrity")

# 3

total = float(input("Enter your Zomato order total: "))

if total > 299:
    print("Apply Free Delivery")
elif total >= 200:
    print("Add more items for free delivery")
else:
    print("Delivery charges apply")


# 4

cart_value = float(input("Enter cart value: "))
payment = input("Enter payment method (UPI/Card/Cash): ")

if cart_value > 1000:
    if payment == "UPI":
        print("Eligible for 10% cashback")
    else:
        print("Eligible for 5% cashback")
else:
    print("No cashback")



