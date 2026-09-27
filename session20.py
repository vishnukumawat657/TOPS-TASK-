# 1
class Product:

    def __init__(self, price):
        self._price = price

    def display_price(self):
        print("Price:", self._price)


product = Product(500)
product.display_price()

# 2
class Playlist:

    def __init__(self):
        self._songs = []

    # Add song
    def add_song(self, song):
        self._songs.append(song)

    # Remove song
    def remove_song(self, song):
        self._songs.remove(song)

    # Get songs
    def get_songs(self):
        return self._songs


playlist = Playlist()

playlist.add_song("Kesariya")
playlist.add_song("Believer")
playlist.add_song("Perfect")

print("Songs:", playlist.get_songs())

playlist.remove_song("Believer")

print("After removing:", playlist.get_songs())


# 3
class Playlist:

    def __init__(self):
        self._songs = []

    # Add song
    def add_song(self, song):
        self._songs.append(song)

    # Remove song
    def remove_song(self, song):
        self._songs.remove(song)

    # Get songs
    def get_songs(self):
        return self._songs


playlist = Playlist()

playlist.add_song("Kesariya")
playlist.add_song("Believer")
playlist.add_song("Perfect")

print("Songs:", playlist.get_songs())

playlist.remove_song("Believer")

print("After removing:", playlist.get_songs())


# 4
from abc import ABC, abstractmethod


class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(PaymentMethod):

    def pay(self, amount):
        print("Payment of ₹", amount, "processed using UPI")


class CreditCard(PaymentMethod):

    def pay(self, amount):
        print("Payment of ₹", amount, "processed using Credit Card")


# Create objects
upi = UPI()
card = CreditCard()

upi.pay(500)
card.pay(1000)
