class SuperList(list):
    def __len__(self):
        return 1000

super_list1 = SuperList();
 #   def append(self,numberto):
        


print (len(super_list1))
super_list1.append(5)
super_list1.append(6)
super_list1.append(3)
#super_list1.sort()     
print(super_list1[0])
print(super_list1[1])

print(issubclass(list,object))
