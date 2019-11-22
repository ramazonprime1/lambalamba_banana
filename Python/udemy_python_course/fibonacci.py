series = []
singlenum = []

def addit(num1):
    single = []
    for item in str(num1):
        single.append(int(item))
    mingle = sum(single)
    return mingle

def fibonacci(enum):
    print ("\n--------\n")
    series.append(1)
    series.append(1)
    [series.append(series[k-1]+series[k-2]) for k in range(enum)]
    print (series)
    
    for num1 in series:
        if num1 > 9:
           while True:
                if num1 > 9:
                   final = addit(num1) 
                break
                singlenum.append(final)
        else:
            singlenum.append(num1)
    print ("\n--------\n")
    print (singlenum)


    



fibonacci(int(input("enter the fibonacci sequence size\n")))
