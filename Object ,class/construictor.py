class student:
    name = " "
    roll = ""

    def __int__(self,name ,roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(f"Name ->{self.name}, Roll number ->>{self.roll}")

std1 = student("Sajjad Jim",5364)
std1.display()

std2 =  student("Siam",101)
std2.display()
