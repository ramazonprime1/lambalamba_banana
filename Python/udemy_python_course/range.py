user = {
    'name' : 'Goliath',
    'age' : 5189,
    'can_swim' : False
}

print(range(10))

for _ in range(4,10,2):
    print (_)

for _ in range(10,0,-1):
    print (_)

for _ in range(3):
    print (list(range(10)))

for r, name in enumerate(user.items()):
                # the above enumerate option would give the iteration number and items in tuple
    print (r, name)

for r, name in enumerate(user.items()):
                # the above enumerate option would give the iteration number and items without tuples involved.
    key, value = name
    print (r, key, value)

for r, numr in enumerate(range(10)):
    if numr == 5:
       print ("the index of " + str(numr) + " is " + str(r))
       print (f'the index of {numr} is {r}')
