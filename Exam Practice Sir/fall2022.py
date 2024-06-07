class StarBuck:
    coffee={
    'latte':100,
    'black':70,
    'regular':80,
    'americano':120,
    'cappuccino':150,
    'espresso':100,
    }
    
    def __init__(self):
        self.order1=''
        self.quantity1=0
        self.order2=''
        self.quantity2=0
        self.order3=''
        self.quantity3=0
        self.ratings=0


    def details(self,order1,quantity1,order2,quantity2,order3,quantity3):
        self.order1=order1
        self.quantity1=quantity1
        self.order2=order2
        self.quantity2=quantity2
        self.order3=order3
        self.quantity3=quantity3
        self.total=self.quantity1*self.coffee[order1]+self.quantity2*self.coffee[order2]+self.quantity3*self.coffee[order3]
        self.orders={}
        self.orders.update({order1:self.coffee[order1]})
        self.orders.update({order2:self.coffee[order2]})
        self.orders.update({order3:self.coffee[order3]})
        final=sorted(self.orders.items(),key=lambda x:x[1])
        print(f"Your orders are ")
        for key in final:
            print(f"{key}")
        print(f"Your total is {self.total}")
        

    def deliver(self):
        print(f"Your order will be delivered in 30 minutes")

    def rating(self,ratings):
        self.ratings=ratings
        print(f"Customer gave a {self.ratings}")





customer=StarBuck()
print("The Menus: Latte:100,black:70,regular:80,americano:120,cappuccino:150,espresso:100,")
print("<---Please enter your choice and quantity--->")
order1=input("Please Enter the coffee Name:")
quantity1=int(input("Please Enter the Quantity:"))
order2=input("Please Enter the coffee Name:")
quantity2=int(input("Please Enter the quantity:"))


# customer.details('latte',2,'black',1,'regular',3)
customer.details(order1,quantity1,order2,quantity2)
customer.deliver()

rat=int(input("Please give a rating from 1 to 5:"))
customer.rating(rat)