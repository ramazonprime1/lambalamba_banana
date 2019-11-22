my_list = [5,4,3]
hislist = list(map(lambda item: item**2, my_list))

print (hislist)

                # Sort a list using Lambda functions
sortit = [(0, 2), (4, 3), (10, -1), (9, 9)]
sortit.sort(key=lambda x: x[1])
print (sortit)