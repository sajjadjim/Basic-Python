class TriAngle :
    def __init__(self ,base, height , ):
        self.base = base
        self.height = height

    def Calculate(self):
        area = 0.5 * self.base * self.height
        print(f"Area Print ->{area}")

t1 = TriAngle(5,6)
t1.Calculate()

t2 = TriAngle(10,10)
t2.Calculate()