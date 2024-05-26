class student:
    name = " "
    roll = ""

    def set_Value(self,name , roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(f"Name ->{self.name}, Roll number ->>{self.roll}")

std1 =  student()
std1.set_Value("Sajjad Hossain jim" ,5364)
std1.display()

std2 =  student()
std2.set_Value("Siam",101)
std2.display()
