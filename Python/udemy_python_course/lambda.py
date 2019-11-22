from functools import reduce
                # lambda arguments : expression
                # lambda param : action(param)
                # The Map map(function, iterable)
                # Map can only process iterables
                # Lambda can process arguments and has nothing to do with reduce method.
my_list = [1,2,3,4,5,6,7,78,889,55432] 
my_number = 99               
print (list(map(lambda item: item/2, my_list)))
#print (int(map(lambda utem: utem/3, my_number)))
print (my_list)
print (my_number)

print ("entering a simple use of lambda")

add = lambda x, y : x + y

print (add(3,my_number))

map_output = map(lambda x: x*2, [1, 2, 3, 4])
print(map_output) # Output: map object: <map object at 0x04D6BAB0>

list_map_output = list(map_output)

print(list_map_output)
                # The Filter
alist = [1,33,32,24,35,76,87,88]

print (list(filter(lambda item : item%2 == 0, alist)))

dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
  
print (list(map(lambda x : x['name'], dict_a)))
  
print (list(map(lambda x : x['points']*10,  dict_a)))

print (list(map(lambda x : x['name'] == "python", dict_a)))

square_cube_list = [[a**2,a**3] for a in alist]

print (square_cube_list)

list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]

common_numbers = [a for a in list_a for b in list_b if a == b]
print (common_numbers)

even_numbers_list_comprehensions = [a for a in list_a if a%2 == 0]

print (even_numbers_list_comprehensions)

uncommon_numbers = [a for a in list_a for b in list_b if a != b]
print (set(uncommon_numbers))


                # The Reduce using Lambda
def accumulator(acc, item):
    print (acc, item)
    return acc+item

print (reduce(lambda acc, item: acc+item, my_list))

print (my_list)
