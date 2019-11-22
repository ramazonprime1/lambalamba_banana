#import someclass

def test_names_cities(john,macy,irving):
    print("john's:", john, "\nmacy: ", macy, "\nirving: ", irving)

cities = ("nyc","bombay","delhi")

test_names_cities(*cities)

names_and_cities = {"irving": "hyderabad", "john": "chennai", "macy": "yerpedu"}

test_names_cities(**names_and_cities)

def get_info(self, *args):
    return "test data is here"
#someclass.get_info = get_info