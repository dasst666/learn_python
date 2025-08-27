# Code and train OOP 
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        return f"This is {self.restaurant_name} its {self.cuisine_type}"

    def open_restaurant(self):
        return "Restaurant open"

my_rest = Restaurant("CiaoCacao", "Italian bystro food")
print(my_rest.describe_restaurant())

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors = None):
        super().__init__(restaurant_name, cuisine_type)
        if flavors is None:
            self.flavors = []
        else:
            self.flavors = flavors

    def all_flavours(self):
        if not self.flavors:
            return "No flavors available"
        else:
            return [f"Available flavours is: {flavor}" for flavor in self.flavors]

my_ice_rest = IceCreamStand("Cold", "Ice cream magazine", ["Vanilla", "Bublegum"])
print(my_ice_rest.all_flavours())

#---------------------------------------------------------------------------------------
class Privileges():
    def __init__(self, privileges = None):
        if privileges is None:
            self.privileges = {"can_delete", "can_edit", "can_ban"}
        else:
            self.privileges = set(privileges)
        
    def show_privileges(self):
        privileges_list = "\n".join(f"- {p}" for p in self.privileges)
        return f"Your previlegies is: \n{privileges_list}"

class User():
    def __init__(self, name, email):
         self.name = name
         self.email = email
    
    def say_hello(self):
        return f"Hello dear {self.name}"

class Admin(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.privileges = Privileges()

my_admin = Admin("Dastan", "das@email.com")
print(my_admin.privileges.show_privileges())
print(my_admin.privileges.privileges)
    
#---------------------------------------------------------------------------------------

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

class Battery():
    def __init__(self, range = 260, battery_size=75):
        self.battery_size = battery_size
        self.range = range

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        if self.battery_size == 75:
            self.range = 260
            print(f"This car can go about {self.range} miles on a full charge.")
        elif self.battery_size == 100:
            self.range = 315
            print(f"This car can go about {self.range} miles on a full charge.")
    
    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100
        return self.battery_size

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

