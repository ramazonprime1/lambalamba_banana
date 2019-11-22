picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
#scan and print a picture

for i in range(3):
    pic = []
    for item in picture:
        for image in item:
            if image == 0:
                print (" ", end='')
            else:
                print ("*", end='')
        print ('')

'''
pic = []
for item in picture:
    for image in item:
        if image == 0:
            print (" ", end='')
        else:
            print ("*", end='')
    print ('')
    '''