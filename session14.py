# 1
songs = ["Kesariya", "Believer", "Shape of You", "Excuses", "Perfect"]

file = open("my_playlist.txt", "w")

for song in songs:
    file.write(song + "\n")

file.close()

print("File created successfully")

# 2
file = open("my_playlist.txt", "r")

for song in file:
    print(song.strip().upper())

file.close()

# 3
import csv

file = open("ipl_scores.csv", "r")

reader = csv.DictReader(file)

for row in reader:
    print("Winner:", row["Winner"])

file.close()

# 4




# 5
from pathlib import Path

file = Path("zomato_orders.json")

if file.exists():
    print("zomato_orders.json file is found")
else:
    print("zomato_orders.json file is not found")

    