                # List, Set, Dictionary
my_list = []                

for char in 'hello':
    my_list.append(char)

print (my_list)

                # [param for param in 'iterable']
my_list = [char for char in 'german']

print (my_list)

my_list2 = [num for num in range(50, 100)]

my_list3 = [num*num for num in range(50, 100) if num % 2 == 0]
print (my_list2)
print (my_list3)