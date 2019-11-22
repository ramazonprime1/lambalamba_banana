def checkdriverage(your_age = 0):
    if int(your_age) < 18:
        print ('Sorry, you are too young to drive this car, powering off...')
    elif int(your_age) > 18:
        print ('Powering on, Enjoy the ride!')
    elif int(your_age) == 18:
        print ('Congratulations, on your fist year of driving. Enjoy the ride!')

checkdriverage()
checkdriverage(56)

checkdriverage(int(input("What is your age?: \n")))
