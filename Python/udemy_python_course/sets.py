#set

my_set = {1,2,3,4,5,5,4,2,99}
print (my_set)

ur_set = {4,6,7,8,4,4,6,9,23,4}

#my_array = [12,12,12,34,34,2,3,4]
my_array = {12,12,12,34,6,34,2,3,4}

my_sets = set(my_array)

print (my_sets)

print(len(my_set))

print (my_set.difference(ur_set))

ur_set.discard(23)
print (ur_set)

print (my_array.intersection(ur_set))
print (ur_set.intersection(my_array))

print (my_array.union(ur_set))
print (ur_set.union(my_array))

#my_set.difference_update(ur_set)

#print (my_set)

