class ShoppingCart:

    def __init__(self):
        self.__items = []
        self.__total_price = 0.0

    def add_item(self, name, price):
        if price > 0:
            self.__items.append((name, price))
            self.__total_price += price
            print(f"Item '{name}' added to the cart")
        else:
            print("Invalid price. Cannot add item.")

    def remove_item(self, name):
        for item in self.__items:
            if item[0] == name:
                self.__items.remove(item)
                self.__total_price -= item[1]
                print(f"Item is removed from the cart {item}")
                return
        print("Item not found in cart.")

    def get_items(self):
        return self.__items

    def get_total_price(self):
        return self.__total_price

grocery=ShoppingCart()
grocery.add_item("Dhall",155)
grocery.add_item("Rice",75)

print("Item to remove: ", grocery.remove_item("Dhall"))

print("Cart Items: ",grocery.get_items())
print("Cart Items: ",grocery.get_total_price())

