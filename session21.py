# 1
class Product:
    def get_discount(self):
        return 0


class Electronics(Product):
    def get_discount(self):
        return 10


p = Product()
e = Electronics()

print("Product discount:", p.get_discount(), "%")
print("Electronics discount:", e.get_discount(), "%")

# 2
class FoodOrder:
    def calculate_total(self, price):
        return price


class ZomatoOrder(FoodOrder):
    def calculate_total(self, price):
        return price + (price * 0.05)


order = FoodOrder()
zomato = ZomatoOrder()

print("Food Order Total:", order.calculate_total(1000))
print("Zomato Order Total:", zomato.calculate_total(1000))

# 3
class Influencer:
    def bonus(self):
        return 2000


class BrandManager:
    def bonus(self):
        return 5000


def show_bonus(employee):
    print("Bonus:", employee.bonus())


influencer = Influencer()
manager = BrandManager()

show_bonus(influencer)
show_bonus(manager)

# 4
class User:
    def get_status(self):
        return "active"


class PremiumUser(User):
    def get_status(self):
        return "premium"


user = User()
premium_user = PremiumUser()

print("User Status:", user.get_status())
print("Premium User Status:", premium_user.get_status())