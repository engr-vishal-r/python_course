from abc import ABC, abstractmethod

class Restaurant(ABC):

    @abstractmethod
    def customer_view(self):
        pass

    @abstractmethod
    def _admin_view(self):
        pass


class Customer(Restaurant):

    def __init__(self, name, orders, final_amount):
        self.name = name
        self.orders = orders
        self.final_amount = final_amount

    def customer_view(self):
        return {
            "fullname": self.name,
            "orders": self.orders,
            "finalAmount": self.final_amount
        }

    def _admin_view(self):
        # Customers shouldn't access this
        raise NotImplementedError("Customer cannot access admin view")


class Admin(Restaurant):

    def __init__(self, name, orders, discount, full_amount, final_amount):
        self.name = name
        self.orders = orders
        self.discount = discount
        self.full_amount = full_amount
        self.final_amount = final_amount

    def customer_view(self):
        return {
            "fullname": self.name,
            "orders": self.orders,
            "finalAmount": self.final_amount
        }

    def _admin_view(self):
        return {
            "fullname": self.name,
            "orders": self.orders,
            "discountAmount": self.discount,
            "fullAmount": self.full_amount,
            "finalAmount": self.final_amount
        }


# Example usage
cust = Customer("Ramesh", ["Pizza", "Soda"], 400)
admin = Admin("Ramesh", ["Pizza", "Soda"], 100, 500, 400)

print("Customer View:", cust.customer_view())
print("Admin View:", admin._admin_view())