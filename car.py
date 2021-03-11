class Car:
	"""A simple attempt to represent a car """

	def __init__(self, make, model, year, manufaturer, ):
		"""Initialized attributes to described a car"""
		self.make = make
		self.model = model
		self.year = year
		self.manufaturer = manufaturer
		self.odometer_reading = 0

	def	get_descriptive_name(self):
		"""Return a netly formated descriptive name"""
		long_name = f"{self.year} {self.manufaturer} {self.model}"
		return long_name.title()

	def read_odometer(self):
		"""Print a statement showing the car mileage"""
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		"""Set the odometer reading to the given value """
		self.odometer_reading = mileage

	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading """
		self.odometer_reading += miles


class Battery:
	"""A sinple attempt to model a baterry for an electric car."""

	def __init__(self, battery_size=75):
		"""Initialized the battery attributes"""
		self.battery_size = battery_size

	def described_battery(self):
		"""Print a statemn descin=bing the batery size """
		print(f"this car has a {self.battery_size}-kwh battery")

	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315
			print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
	"""Represent aspect of car, specific to electric vehicles """

	def __init__(self, make, model, year):
		"""intialized attribute of the parent class """
		super().__init__(self, make, model, year)
		self.baterry = Battery()
	def described_battery(self):
		"""print a statement describing the battery size """
		print(f"This car has a {self.battery_size}.kwh battery.")

	def fill_gas_tank(self):
		"""Electric cars don't have gas tanks."""
		print("This car doesn't need a gas tank!")

# my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.baterry.described_battery()
# my_tesla.baterry.get_range()

# my_new_car = Car('audi', 'a4', 2019, 'audi')
# print(my_new_car.get_descriptive_name())
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()

# my_used_car = Car('subaru', 'outback', 2015, 'subaru')
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()	