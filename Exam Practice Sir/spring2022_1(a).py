class BankUser:
    def __init__(self):
        self.balance=0
        self.name=""

    def user_details(self,name):
        self.name=name
        print(f"User name: {self.name}")
        print(f"Balance: {self.balance}")

    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"Amount deposited: {amount}")
        print(f"Balance: {self.balance}")

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance=self.balance-amount
            print(f"Amount withdrawn: {amount}")
            print(f"Balance: {self.balance}")
        else:
            print("Insufficient balance")

user=BankUser()

user.user_details("Rahul")

user.deposit(1000)
user.withdraw(500)