'''1.
Create three variables in Python: user_name, fav_app, and daily_usage_hours. Assign your own name, your favorite app (like Instagram or Zomato), and how many hours you use it daily.
2.
Write a Python script that declares variables for product_name, price, and is_available to represent an item on Flipkart. Print each variable and its data type using the type() function.
3.
Demonstrate the difference between single-line and multi-line comments in Python by writing a script that explains how a Spotify playlist recommendation system might work. Use # for single-line and triple quotes for multi-line comments.
4.
Create variables for order_total, delivery_region, and discount_percent to represent a Zomato order. Follow Python naming conventions and print a sentence using all three variables, like 'Order from [region] totals ₹[order_total] with [discount_percent]% discount.'
5.
Write a Python script that intentionally mixes tabs and spaces for indentation, then fix the 
script so it runs without errors.<br><br><em><strong>Hint:</strong> Use only spaces for indentation,
 as per Python's best practices.</em>
'''
# 1
user_name = "Vishnu"
fav_app = "Instagram"
daily_usage_hours = 3

print(user_name)
print(fav_app)
print(daily_usage_hours)


# /2
product_name = "Laptop"
price = 45000.50
is_available = True

print(product_name, type(product_name))
print(price, type(price))
print(is_available, type(is_available))

# 3
# Spotify recommends songs based on your listening history.

"""
Spotify can recommend songs by checking:
1. Songs you listen to
2. Your favorite artists
3. Your playlists
4. Similar users' listening habits
"""

print("Spotify Playlist Recommendation")

# 4
order_total = 500
delivery_region = "Ahmedabad"
discount_percent = 10

print(f"Order from {delivery_region} totals ₹{order_total} with {discount_percent}% discount.")

# 5
if True:
    print("Hello")
    print("Python")