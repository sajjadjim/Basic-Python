class Employee:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.salary=0
        

    def employee_details(self):
        print(f"Employee name: {self.name}")
        print(f"Employee email: {self.email}")
        print(f"Employee salary: {self.salary}")

    def check_in(self):
        print("Employee is checked in at 9 am")

    def check_out(self):
        print("Employee is checked out at 5 pm")

class Faculty(Employee):
    def __init__(self,name,email):
        super().__init__(name,email)
        self.salary=30000

    def conduct_class(self):
        print(f"{self.name} is conducting class")

    def couselling_student(self):
        print(f"{self.name} is couselling student")

    def salary_details(self):
        print(f"{self.name}'s previous salary: {self.salary}")
        print(f"{self.name}'s new salary: {self.salary + 0.1*self.salary}")



    #(iii) ans: new checkin checkout for faculty 
    def check_in(self):
        print("Faculty is checked in at 9:30 am")

    def check_out(self):
        print("Faculty is checked out at 5:30 pm")

class Admin(Employee):
    def __init__(self,name,email):
        super().__init__(name,email)
        self.salary=35000

    def management_campus(self):
        print(f"{self.name} is managing campus")

    def monitor_student(self):
        print(f"{self.name} is monitoring student") 

    def salary_details(self):
        print(f"{self.name}'s previous salary: {self.salary}")
        print(f"{self.name}'s new salary: {self.salary + 0.15*self.salary}")


    #(iii) ans: new checkin checkout for admin
    def check_in(self):
        print("Admin is checked in at 8 am")

    def check_out(self):
        print("Admin is checked out at 6 pm")


roshna=Faculty("Roshna","roshna@gmail.com")
roshna.employee_details()
roshna.check_in()
roshna.check_out()
roshna.conduct_class()
roshna.couselling_student()
roshna.salary_details()

rahim=Admin("Rahim","rahim@gmail.com")

rahim.employee_details()
rahim.check_in()
rahim.check_out()
rahim.management_campus()
rahim.monitor_student()
rahim.salary_details()



