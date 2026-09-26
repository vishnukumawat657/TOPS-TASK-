# 1
followers = 1200
rating = 4.5
app_name = "Spotify"
is_premium_user = True

print(followers, type(followers))
print(rating, type(rating))
print(app_name, type(app_name))
print(is_premium_user, type(is_premium_user))


# 2

price = input("Enter Zomato order price: ")

price = float(price)

gst = price * 18 / 100
final_bill = price + gst

print("Final bill:", final_bill)


#3

prices = ['199.99', '299.50', '150']

prices = [float(x) for x in prices]

total = sum(prices)

print("Total cart value:", total)


#4

def is_discount_applicable(order_amount):
    if order_amount > 500:
        return True
    else:
        return False

print(is_discount_applicable(450))
print(is_discount_applicable(750))



#5

ratings = ['4.5', '3.0', '5', '4.2']

ratings = [float(x) for x in ratings]

highest = max(ratings)

print("Highest rating:", highest)