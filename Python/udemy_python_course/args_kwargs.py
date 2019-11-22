def super_func(name,*args,comment='hi',**kwargs):
    total = 0
    print (comment)
    for items in kwargs.values():
        total += items
        print (items)
    return sum(args) + total

print (super_func('rajesh',1,2,3,4,5,num1=10,num2=30))

                # Rule: params, *args, default parameters, **kwargs