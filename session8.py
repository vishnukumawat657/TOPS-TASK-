# 1

order_amounts = [120, 250, 90, 310, 150]

total = 0

for amount in order_amounts:
    total = total + amount

print("Total order value:", total)

# 2

scores = [45, 78, 102, 34, 67, 89]

i = 0

while i < len(scores):
    if scores[i] > 100:
        break

    print(scores[i])
    i = i + 1

# 3

prices = [299, 499, 199, 999, 149]

total = 0

for price in prices:
    if price < 200:
        continue

    total = total + price

print("Total:", total)

# 4
songs = ['Kesariya', 'Believer', 'Shape of You', 'Blinding Lights', 'Excuses']

for position, song in enumerate(songs, start=1):
    print(position, song)


# 5

followers = [120, 1500, 23000, 800, 45000]

for count in followers:

    if count < 1000:
        print("Micro")

    elif count <= 10000:
        print("Influencer")

    else:
        print("Celebrity")