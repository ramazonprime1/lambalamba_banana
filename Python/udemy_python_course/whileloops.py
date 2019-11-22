my_list = [1,2,3]

for item in my_list:
    print (item)

print ("-------------------")

i = 0

while i < len(my_list):
    print (my_list[i])
    i += 1

while True:
    response = input ('say hi or bye: ')
    if (response == 'bye'):
        print ("ok bye")
        break


for item in my_list:
    pass
print ("pass complete")

for item in my_list:
    continue
                # will allows the for/while loop to continue through the loop without running through the remaining code after continue until the loop is done.
    print (item)


while True:
    response = input ('say hi or bye: ')
    if (response == 'bye'):
        print ("ok bye")
        break
