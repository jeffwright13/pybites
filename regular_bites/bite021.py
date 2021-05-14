"""
Bite 21. Query a nested data structure

Given the provided cars dictionary:

    Get all Jeeps
    Get the first car of every manufacturer.
    Get all vehicles containing the string 't|Trail' in their names (should work for other grep too)
    Sort the models (values) alphabetically

See the docstrings and tests for more details. Have fun!

Update 18th of Sept 2018: as concluded in the forum it is better to pass the cars dict into each function to make its scope local.
"""
CARS = {
    "Ford": ["Falcon", "Focus", "Festiva", "Fairlane"],
    "Holden": ["Commodore", "Captiva", "Barina", "Trailblazer"],
    "Nissan": ["Maxima", "Pulsar", "350Z", "Navara"],
    "Honda": ["Civic", "Accord", "Odyssey", "Jazz"],
    "Jeep": ["Grand Cherokee", "Cherokee", "Trailhawk", "Trackhawk"],
}


def get_all_jeeps(cars=CARS):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    return ", ".join(cars["Jeep"])


def get_first_model_each_manufacturer(cars=CARS):
    """return a list of matching models (original ordering)"""
    return [cars[key][0] for key in cars.keys()]


def get_all_matching_models(cars=CARS, grep="trail"):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    pass


def sort_car_models(cars=CARS):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    pass
