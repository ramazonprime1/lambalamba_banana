def pi_value():
    pi = 22/7
    print (pi)
    
pi_value()
                #simple function

                #parameters: When defining
                #arguments: when calling, invoking the functions

def class_name(name, grade):
    print (f'His name is {name} and he is in {grade}')

class_name('rajesh', 4)
                #calling a function using positional arguments

def animal_weight(animal, weight):
    print (f'the animal name is {animal} and it\'s weights is {weight}')

animal_weight(animal='giraffe', weight='2T')
                #function using keyword arguments, this is not recommended
            
def game_company(game_name='cricket', company_name='EA Sports'):
    print (f'the game name is {game_name} and the gaming studio is {company_name}')

game_company('Red Dead Redemption 2', 'Rock Star Games')
                # function using default parameters, default parameters come into play when arguments are missing.

def sum (num1,num2):
    num1 + num2

print (sum(4,5))

def multiply (num1,num2):
    return num1 * num2

total = multiply(3,9)
print (multiply(4,total))
                # Calling a function within a function using a variable.

def divideit(num1,num2):
    def division2(n1,n2):
        return n1/n2
    return division2(num1,num2)
                # The result of dicision2 function is returned to the divideit function and thus return will exit the function.
    return 5
                # This return will never execute
    print ('hello')
                # This print statement will never execute

print (int(divideit(10,5)))
