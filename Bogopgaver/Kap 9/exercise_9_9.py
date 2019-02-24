"""9-9. Battery Upgrade
Use the final version of electric_car.py from this section.
Add a method to the Battery class called upgrade_battery().
This method should check the battery size and set the capacity to 85 if it isn’t already.
Make an electric car with a default battery size, call get_range() once,
and then call get_range() a second time after upgrading the battery.
You should see an increase in the car’s range."""


class Car():
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=60):
        """Initialize the batteery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):  #new method added doing this exercise
        """method to upgrade the battery to 85 if it isn't already
        Note the method actually downgrades the battery if it is already larger than 85."""
        if self.battery_size != 85: #the method only does anything if the battery size is not already 85.
            self.battery_size = 85
        else:
            print("Battery is already upgraded")

class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()

#creating electric car and checking range:
ellert = ElectricCar("ellert", "ellert", 1985)
ellert.battery.get_range()

#upgrading the battery and checking range
ellert.battery.upgrade_battery()
ellert.battery.get_range()