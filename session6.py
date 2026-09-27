# 1

playlist_prices = {
    "Bollywood Hits": 99,
    "English Songs": 149,
    "Punjabi Hits": 129,
    "Workout Music": 199,
    "Romantic Songs": 159
}

print(playlist_prices)


# 2

playlist_prices = {
    "Workout": 100,
    "Chill": 150,
    "Party": 200,
    "Study": 120,
    "Romantic": 180
}

def update_playlist_price(playlist, new_price):
    playlist_prices[playlist] = new_price


update_playlist_price("Workout", 250)


print(playlist_prices)

# 3
playlist_prices = {
    "Workout": 100,
    "Chill": 150,
    "Party": 200,
    "Study": 120,
    "Romantic": 180
}


del playlist_prices["Party"]

print(playlist_prices)

# 4

set1 = {"Dominos", "Pizza Hut", "McDonalds", "Burger King"}
set2 = {"McDonalds", "Burger King", "Subway", "KFC"}


print("Union:", set1.union(set2))


print("Intersection:", set1.intersection(set2))
