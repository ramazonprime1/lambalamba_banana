#DRY
#python code for printing duplicates in a list.

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

'''
i = 1
new_list = []

while i < len(some_list):
    item = some_list[i]
    for stuff in some_list:
        if stuff == item and item != some_list[i]:
           print (f'this is repeting ** {stuff}')
           new_list.append(stuff)
    i += 1
print (new_list)

def Repeat(x): 
    _size = len(x) 
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    return repeated 
  
print (Repeat(some_list)) 
'''
def duplicate(x):
    dups = []
    for value in some_list:
        if some_list.count(value) > 1 and value not in dups:
           dups.append(value)
    return dups

print (duplicate(some_list))

