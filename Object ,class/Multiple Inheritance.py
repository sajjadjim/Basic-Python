class A:
    def display1(self):
        print("I am in A class.......")

class B():
    def display2(self):
        print("I am in B class.......")

class C(A,B):
    def display3(self):
        super().display1()
        self.display2()  # Call display2 directly from self
        print("I am in C class.......")

c1 = C()
c1.display3()
