info = ('y','yes')
queue = 'yes'
janus = 2

if queue and janus:
    if queue in info and janus == 2:
        print ('tuple works')
    else:
        print ('wrong data')
else:
    print ('please fill the form')