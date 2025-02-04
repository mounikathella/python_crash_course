class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
     self.odometer_reading += miles

class Battery:
    def upgrade_battery(self):
        if not self.battery_size:
            self.battery_size = 100



class electric_car(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 0
    def describe_battery(self):
        print("This car is a battery of " + str(self.battery_size) + " - kwh battery.")
    battery = Battery()

my_tesla = electric_car("Tesla","Model s",2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.upgrade_battery()


# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#         self.name = restaurant_name
#         self.type = cuisine_type
#         self.number_served = 0
#     def describe_restaurant(self):
#         print(self.name.title() + " is the restaurant name.")
#         print("The cuisine type is " + self.type.title() + ".")

#     def open_restaurant(self):
#         print("Our restaurant " + self.name.title() + " is open today.")

#     def num_served(self):
#         print("The number of people served are " + str(self.number_served))

#     def set_number_served(self,people):
#         self.number_served = people
    
#     def increment_number_served(self,inc_people):
#         self.number_served += inc_people

# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name, cuisine_type):
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = ["venila","chocolate","strawberry","butterscotch","pinapple"]
#     def display_flavors(self):
#         print("The icecream flavors are: \n")
#         for i in self.flavors:
#             print("-" + i)

# icecream = IceCreamStand("Ibaco","Icecreams")
# icecream.display_flavors()

# class User():
#     def __init__(self,first_name,last_name,age,city):
#         self.f_name = first_name
#         self.l_name = last_name
#         self.age = age
#         self.city = city
#         self.qualification = "Degree"
#         self.login_attempts = 0
#     def describe_user(self):
#         print("The username is " + self.f_name.title() + " " + self.l_name.title() + " of age " + self.age + " lives in " + self.city)

#     def greet_user(self):
#         print("Hello " + self.f_name.title() + " " + self.l_name.title() + "!")

#     def user_qualification(self):
#         print(self.f_name.title() + " " + self.l_name.title() + " has studied " + self.qualification)

#     def increment_login_attempts(self):
#         self.login_attempts += 1
    
#     def reset_login_attempts(self):
#         self.login_attempts = 0

# class Privileges:
#     privileges = ["can add post","can delete post","can ban user"]
#     def show_privileges(self):
#         for i in self.privileges:
#             print("-" + i)

# class Admin(User):
#     def __init__(self, first_name, last_name, age, city):
#         super().__init__(first_name, last_name, age, city)
#         self.privileges = Privileges()
        


# admin = Admin("admin","ADMIN", 24, "Tampa")
# admin.privileges.show_privileges()
