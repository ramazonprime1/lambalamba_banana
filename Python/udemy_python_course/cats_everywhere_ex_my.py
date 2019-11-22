#Given the below class:
class cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = cat('edward',6)
cat2 = cat('thomas',4)
cat3 = cat('Julius',5)

# 2 Create a function that finds the oldest cat
def oldcat(*cats):
  ages = []
  for age in cats:
    ages.append(age)
    ages.sort()
  return ages[-1]

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

oldcat = oldcat(cat1.age,cat2.age,cat3.age)

print (f'The oldest cat is {oldcat} years old')