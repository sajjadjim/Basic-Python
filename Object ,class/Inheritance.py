class phone :
    def call(self):
        print("ANy one Can call in phone ...........")

    def picture(self):
        print("Any one can take photo with phone......")


class  pixel(phone):
    def name(self):
        print("pixel 6 phone...........")

pixel1 = pixel()
pixel1.name()
pixel1.call()
pixel1.picture()