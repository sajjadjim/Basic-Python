class shape:
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2

    def area(self):
        print("I am area method of shape class")


class triangle(shape):
    def area(self):
        area= 0.5 * self.dim1 * self.dim2
        print("Area of Triangle :", area)


class rectangle(shape):
    def area(self):
        area= self.dim1 * self.dim2
        print("Area of rectangle :", area)

t1=triangle(20,30)
t1.area()
r1=rectangle(20,30)
r1.area()