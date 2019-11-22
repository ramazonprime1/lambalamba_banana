#Given the below class:
class cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = cat('Rambo',2)
cat2 = cat('thomas',4)
cat3 = cat('Julius',5)
dog = [cat1, cat2, cat3]
cat_dict = {}
for acat in dog:    
   cat_name =acat.name
   cat_age = acat.age
   cat_dict[cat_name] = cat_age
print(cat_dict)

def oldcat_name(catz):
    sort_cat = []
    sort_cat = sorted(catz.values())
    print (sort_cat)
    for namer, ager in catz.items():
        if ager == sort_cat[-1]:
            print (f'this is the oldest cat name {namer} with an age of {ager}')

oldcat_name(cat_dict)

            