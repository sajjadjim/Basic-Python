from datetime import datetime
# Base class for Vehicle
class Vehicle:
    def __init__(self, registration_number, model_number, year_of_manufacture, rental_fee):
        self.registration_number = registration_number
        self.model_number = model_number
        self.year_of_manufacture = year_of_manufacture
        self.rental_fee = rental_fee
    def display_info(self):
        print(f"Registration Number: {self.registration_number}")
        print(f"Model Number: {self.model_number}")
        print(f"Year of Manufacture: {self.year_of_manufacture}")
        print(f"Rental Fee: ${self.rental_fee:.2f} per day")

# Subclass for Car
class Car(Vehicle):
    def __init__(self, registration_number, model_number, year_of_manufacture, rental_fee, number_of_doors):
        super().__init__(registration_number, model_number, year_of_manufacture, rental_fee)
        self.number_of_doors = number_of_doors

    def display_info(self):
        super().display_info()
        print(f"Number of Doors: {self.number_of_doors}")

# Subclass for Truck
class Truck(Vehicle):
    def __init__(self, registration_number, model_number, year_of_manufacture, rental_fee, payload_capacity):
        super().__init__(registration_number, model_number, year_of_manufacture, rental_fee)
        self.payload_capacity = payload_capacity

    def display_info(self):
        super().display_info()
        print(f"Payload Capacity: {self.payload_capacity} kg")

# Booking class to manage rentals
class Booking:
    def __init__(self, customer_name, nid, phone_number, vehicle, start_date, end_date, advance_payment=False):
        self.customer_name = customer_name
        self.nid = nid
        self.phone_number = phone_number
        self.vehicle = vehicle
        self.start_date = start_date
        self.end_date = end_date
        self.advance_payment = advance_payment

    def calculate_rental_fee(self):
        duration = (self.end_date - self.start_date).days
        total_fee = duration * self.vehicle.rental_fee
        return total_fee

    def display_booking_info(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"NID: {self.nid}")
        print(f"Phone Number: {self.phone_number}")
        print("Vehicle Information:")
        self.vehicle.display_info()
        print(f"Start Date: {self.start_date.strftime('%Y-%m-%d')}")
        print(f"End Date: {self.end_date.strftime('%Y-%m-%d')}")
        print(f"Advance Payment: {'Yes' if self.advance_payment else 'No'}")
        print(f"Total Rental Fee: ${self.calculate_rental_fee():.2f}")

# Example usage:
if __name__ == "__main__":
    # Create instances of Car and Truck
    car = Car("CAR123", "ModelX", 2021, 50.0, 4)
    truck = Truck("TRK456", "ModelY", 2019, 75.0, 1000)

    # Display vehicle information
    print("Car Information:")
    car.display_info()
    print("\nTruck Information:")
    truck.display_info()
    print("\n")

    # Create a booking for the car
    start_date = datetime(2024, 5, 27)
    end_date = datetime(2024, 5, 30)
    booking = Booking("John Doe", "NID12345", "123-456-7890", car, start_date, end_date, advance_payment=True)

    # Display booking information
    print("Booking Information:")
    booking.display_booking_info()
