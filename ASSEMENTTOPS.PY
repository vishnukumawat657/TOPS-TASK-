# 1
order_value = float(input("Enter order value: Rs "))
distance = float(input("Enter delivery distance: km "))
if order_value < 0 or distance < 0:
    print("Error: Order value and distance cannot be negative.")
else:
   
   if order_value >= 500:
    delivery_fee = 0
   elif distance <= 5:
    delivery_fee = 30
   else:
    delivery_fee = 60
   final_amount = order_value + delivery_fee
print("\n----- FINAL BILL -----")
print(f"Item Total: Rs {order_value:.2f}")
print(f"Delivery Fee: Rs {delivery_fee:.2f}")
print(f"Final Amount Payable: Rs {final_amount:.2f}")



# 2

menu = {
    "Pizza": {"price": 250, "category": "Food"},
    "Burger": {"price": 180, "category": "Snacks"},
    "Pasta": {"price": 200, "category": "Food"},
    "Dosa": {"price": 100, "category": "Breakfast"},
    "Coffee": {"price": 80, "category": "Drinks"},
    "Ice Cream": {"price": 120, "category": "Dessert"}
}


def view_menu():
    print("\n--- MENU ---")

    number = 1

    for dish in menu:
        print(number, dish, "-", menu[dish]["price"])
        number += 1


def filter_category():
    category = input("Enter category: ")

    for dish in menu:
        if menu[dish]["category"] == category:
            print(dish, "-", menu[dish]["price"])


def search_dish():
    dish = input("Enter dish name: ")

    if dish in menu:
        print("Price:", menu[dish]["price"])
    else:
        print("Dish not found")


while True:

    print("\n1. View Menu")
    print("2. Filter Category")
    print("3. Search Dish")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        view_menu()

    elif choice == "2":
        filter_category()

    elif choice == "3":
        search_dish()

    elif choice == "0":
        print("Program End")
        break

    else:
        print("Invalid choice")



# 3


import json

try:
    with open("orders.json", "r") as file:
        orders = json.load(file)

except FileNotFoundError:
    orders = []

customer_name = input("Enter customer name: ")

items = input("Enter items: ").split(",")

try:
    total_amount = float(input("Enter total amount: "))

except ValueError:
    print("Invalid amount")
    exit()

status = input("Enter order status: ")

order = {
    "customer_name": customer_name,
    "items": items,
    "total_amount": total_amount,
    "status": status
}

orders.append(order)

with open("orders.json", "w") as file:
    json.dump(orders, file, indent=4)

print("Order saved successfully!")



# 4


import csv
import os


# Rider class
class Rider:

    def __init__(self, rider_id, name, status="Available", total_deliveries=0):
        self.rider_id = rider_id
        self.name = name
        self.status = status
        self.total_deliveries = total_deliveries

    # Assign order
    def assign_order(self, order_id):
        self.status = "On Delivery"
        print("Order", order_id, "assigned to", self.name)

    # Complete delivery
    def complete_delivery(self):
        self.total_deliveries += 1
        self.status = "Available"
        print("Delivery completed by", self.name)

    # Display rider information
    def display_info(self):
        print("ID:", self.rider_id)
        print("Name:", self.name)
        print("Status:", self.status)
        print("Total Deliveries:", self.total_deliveries)


# Create 3 riders
riders = [
    Rider(1, "Rahul"),
    Rider(2, "Amit"),
    Rider(3, "Vishnu")
]


while True:

    print("\n===== DELIVERY RIDER SYSTEM =====")
    print("1. Assign Order")
    print("2. Complete Delivery")
    print("3. Display Riders")
    print("0. Exit")

    choice = input("Enter choice: ")

    # Assign order
    if choice == "1":

        rider_id = int(input("Enter Rider ID: "))
        order_id = input("Enter Order ID: ")

        for rider in riders:
            if rider.rider_id == rider_id:
                rider.assign_order(order_id)
                break
        else:
            print("Rider not found.")

    # Complete delivery
    elif choice == "2":

        rider_id = int(input("Enter Rider ID: "))

        for rider in riders:
            if rider.rider_id == rider_id:
                rider.complete_delivery()
                break
        else:
            print("Rider not found.")

    # Display riders
    elif choice == "3":

        for rider in riders:
            print("\n----------------")
            rider.display_info()

    # Exit and save CSV
    elif choice == "0":

        with open("riders.csv", "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "rider_id",
                "name",
                "status",
                "total_deliveries"
            ])

            for rider in riders:
                writer.writerow([
                    rider.rider_id,
                    rider.name,
                    rider.status,
                    rider.total_deliveries
                ])

        print("Rider data saved.")
        print("Program ended.")
        break

    else:
        print("Invalid choice.")