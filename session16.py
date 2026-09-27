# 1
movies = ["Jawan", "Pathaan", "Animal", "Dunki", "Fighter"]

movie_iter = iter(movies)

print(next(movie_iter))
print(next(movie_iter))
print(next(movie_iter))
print(next(movie_iter))
print(next(movie_iter))

# 2

songs = [
    "Kesariya",
    "Believer",
    "Shape of You",
    "Excuses",
    "Perfect",
    "Blinding Lights"
]

for position, song in enumerate(songs, start=1):
    print(f"{position}. {song}")

# 3

foods = ["Pizza", "Burger", "Pasta", "Sandwich"]
prices = [250, 120, 180, 100]

for food, price in zip(foods, prices):
    print(f"{food} - ₹{price}")

# 4
def insta_posts_generator(posts):
    for post in posts:
        yield post


posts = [
    "Enjoying my day!",
    "Beautiful sunset",
    "Weekend vibes"
]

post_iter = insta_posts_generator(posts)

try:
    while True:
        print(next(post_iter))

except StopIteration:
    print("All posts displayed")

# 5

def cashback_generator(transactions):
    for amount in transactions:
        yield amount * 0.05


transactions = [200, 500, 1000, 1500, 2000]

for cashback in cashback_generator(transactions):
    print("Cashback: ₹", cashback)