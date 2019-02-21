"""8-14, Cars
Write a function that stores information about a car in a dictionary. the function
should always receive a manufacturer and a model name. It should then accept an
arbitrary number of keyword arguments. Call the function with the required
information and two other name-value pairs, such as a color or an optional
feature. Your function should work for a call like this one:

car = make_car('subaru', 'outback', color='blue', tow_package=True)

Print the dictionary that’s returned to make sure all the information
was stored correctly."""

def make_car(manufacturer, model_name, **features):
    car = {}        #empty dictionary for the car
    car["manufacturer"] = manufacturer  #adding first argument to dictionary
    car["model_name"] = model_name      #adding second argument to dictionary
    for key, value in features.items(): #adding remaining arguments to dictionary
        car[key] = value
    return car

car = make_car("toyota", "camry", color="black", car_thing="a car thing")
print(car)

