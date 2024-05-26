class phone:
    def __int__(self):
        print("I am in the phone class")


class samsung(phone):
    def __int__(self):
        super().__int__()
        print("i am in the samsung class")


s = samsung()