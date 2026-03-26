app_name = 'swiggy' #global variable

def order():
    quantity='2' #local variable
    def menu():
        selected_item='rice' #enhanced variable
        print(f"Customer ordered {quantity} nos. of {selected_item} through {app_name}")

    menu()
order()