class Shop:
    Shop_Name ="\t\tHungry Bite"

    def set_info(self, shop_address , shop_owner):
        self.shop_address = shop_address
        self.shop_owner = shop_owner

    def get_info(self):
        print(f"Shop Address-> {self.shop_address}\nShop owner Name->{self.shop_owner}\n")

class purchase_product(Shop):
    def __init__(self , customer_name ,customer_food , customer_bill , confirm_order):
        self.customer_name = customer_name
        self.customer_food = customer_food
        self.customer_bill =customer_bill
        self.confirm_order = confirm_order

        print(f"Customer Name  --{customer_name}\n Customer Food  --{customer_food}  \nCustomer Bill ---{customer_bill}")

        print(f"Customer Food Order {confirm_order} ")

    def view_shop(self):
        print(f"Welcome to our Shop !!!")

obj1 =Shop()
print(obj1.Shop_Name)
obj1=Shop()
obj1.set_info("Ashula Vanggar potti","Sobur Khan")
obj1.get_info()

obj1.Shop_Name
obj2 =purchase_product("ABCD", "Burger" ,300,"Confirm")
obj3 =purchase_product("XYZ", "Sub-Sanduse---" ,350,"Confirm")
