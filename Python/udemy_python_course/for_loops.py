user = {
    'name' : 'Goliath',
    'age' : 5189,
    'can_swim' : False
}
print("------------------------------------\n")

for item in user.items():
    print(item)
                # prints the key:value pairs in tuples
print("------------------------------------\n")

for name, info in user.items():
    print(name, info)
                # prints the key:value pairs without tuples
print("------------------------------------\n")

for value in user.values():
    print(value)
                # prints the values only
print("------------------------------------\n")
for key in user.keys():
    print(key) 
                # prints the keys only
print("------------------------------------\n")

#iterable: list, dictionary, tuple, set, string
#iterate: one by one check each item in the collection