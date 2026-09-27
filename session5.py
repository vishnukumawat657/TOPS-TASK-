# 1

playlist_ids = [101, 102, 103, 104, 105]

playlist_ids.append(106)

print(playlist_ids)

# 2

cart_items = ['t-shirt', 'shoes']

cart_items.extend(['jeans', 'cap'])

print(cart_items)

# 3

def remove_last_item(order_list):
    return order_list.pop()

order_list = ['pizza', 'burger', 'coke']

removed_item = remove_last_item(order_list)

print("Removed item:", removed_item)
print("Updated order:", order_list)

# 4

insta_filters = ('Vintage', 'Clarendon', 'Juno', 'Lark')

try:
    insta_filters[1] = 'Valencia'
except TypeError as e:
    print("Error:", e)

# Error isliye aata hai kyunki tuple immutable hota hai.


#5

favorite_genres = ['Pop', 'Rock', 'Hip-Hop']


train_classes = ('Sleeper', 'AC 3 Tier', 'AC 2 Tier')