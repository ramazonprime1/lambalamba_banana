#Given the below class:
class cat:
    species = 'mammal'
    def __init__(self, name, age):
        self._name = name
        self._age = age

# Instantiate the Cat object with 3 cats
cat1 = cat('Rambo',2)
cat2 = cat('thomas',4)
cat3 = cat('Julius',5)

# Find the oldest cat
def get_oldest_cat(*args):
    return max(args)

# Output
print(f"The oldest cat is {get_oldest_cat(cat1._age, cat2._age, cat3._age)} years old.")