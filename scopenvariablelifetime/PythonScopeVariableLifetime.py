delivery_partner="Zomato"

def order():
    menu="Biryani"
    def quantity():
        quantity="5"
        print(f"Ordered {quantity} quantity of {menu} through {delivery_partner}")

    quantity()
order()
