# 1
def reverse_string(s):
    if s == "":
        return s
    else:
        return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))

# 2

def sum_playlist_durations(durations):
    if len(durations) == 0:
        return 0
    else:
        return durations[0] + sum_playlist_durations(durations[1:])

durations = [180, 240, 200, 300]

print("Total duration:", sum_playlist_durations(durations), "seconds")

# 3
count = 10

def update_count():
    count = 5
    print("Inside:", count)

update_count()
print("Outside:", count)

# 4
def count_likes(posts):
    total = 0

    for post in posts:
        total += post["likes"]

        if "replies" in post:
            total += count_likes(post["replies"])

    return total


posts = [
    {
        "likes": 10,
        "replies": [
            {"likes": 5},
            {"likes": 3}
        ]
    },
    {
        "likes": 20,
        "replies": [
            {
                "likes": 4,
                "replies": [
                    {"likes": 2}
                ]
            }
        ]
    }
]

print("Total likes:", count_likes(posts))



# 5

app_status = "Offline"

def change_status():
    user_status = "Online"
    
    print("Inside function - user_status:", user_status)
    print("Inside function - app_status:", app_status)


print("Before function - app_status:", app_status)

change_status()

print("After function - app_status:", app_status)

