class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_description(self):
        return f"{self.year} {self.model} {self.make}"
    
    def read_odometer(self):
        print(f"El numero de millas es: {self.odometer_reading}")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles
        
my_car = Car("Toyota", "Camry", 2020)
print(my_car.get_description())
my_car.read_odometer()

my_car.update_odometer(10000)
my_car.read_odometer()

my_car.increment_odometer(200)
my_car.read_odometer()