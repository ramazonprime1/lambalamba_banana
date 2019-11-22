print (2 ** 3)             #gives the output of power.
print (13 // 3)            #rounds the output to the closest integer
print (9 % 4)              #gives the reminder

print (round(7.7))            # rounds the number to the closest integer.
print (abs(-19))           #gives the absolute value of a number

            #Regular expressions.
            #Operator Precedence 
print ((4*5) - 3 * 2 ** 2 / 2 + 12)             #((4 * 5) - (3 * ((2 ^ 2) / 2)) + 12)

# ()
# ^
# *
# /
# X
# -
# +


print (bin(9))
print (int('0b1001101', 2))


language = "english"

print (language)

info = 20

ils = info/33

print (type(ils))

#constants

PI = 3.14 #Giving the variables all CAPS means it should not be assigned again, it is a constant.

#Assigning Values to variables at once

Rajesh, Satish, Mandy = 20, 'sail', 40 + 2 #This is how you assign all variables in one statement

Rajesh = 20
Satish = "sail"
Mandy = 40 + 2 #40+2 is an expression.

print (Rajesh, Satish, Mandy)

# Augmented assignment operator
some_value = 19
some_value *= 40

print (some_value)

long_string = '''
www
o 0
---
'''

print (long_string)

print ("string concatination only works with strings" + "5")

print (type(str(200))) # Type conversion

print ("It\'s nice weather. Well \"Kind of\"...and you need to use a " + "\n\\n") # Escape Sequences

name = "rajesh"
last_name = "kommisetty"
wife_name = "mounika pasupuleti"
age = 35

print ('hi {0}. You are of {1} years old'.format(name, age))

print (f"this is the best format {name[::-1]} for a person of your age of {age}")

# [start:start:stepover] Indices #Also called as Slicing:
print (name[::-1] + " " + last_name[::-1] + " " + wife_name[::-1] + " " + name[::-2])

#Immutable Strings are immutable.

quote = 'to be or not be an idiot. why do you care.'

print (quote.upper())
print (quote.capitalize())
print (quote.find('do'))
print (quote[30:32])
print (quote.replace('do', 'so'))
print (quote)

#booleans

#bool can be True or False

print (str(bool(1)) + " " + str(bool(0)) + "\n")

print (bool('True'))
print (bool('False'))

#Excersice
'''
year_of_birth = input('which year did you born? \n')
   # We are asking the user, which year he was born and assigning the input to a variable
today = 2019
   # This variable is assigned today's year
guessed_age = today - int(year_of_birth)
   # This variable takes the result of the above expression
print (f'Your age may be {guessed_age}')
   # This print function will print the guessed age.
'''

   #password value checker
 
#user_name = input('Please enter your user name \n') 
#password = input('Please enter your password\n')
#lpassword = len(password)
#mask_password = '*' * int(lpassword)

#print (f'Dear {user_name}, your password is {mask_password} which is {lpassword} chars long')

#print (
    #'''
    #www
   # - O
  #  ---
 #   '''
#)
#

shopping_cart = [
        'notes', 
        'glasses', 
        'shoes',
        'books'
        ]

old_cart = [
        'weights', 
        'dumbels', 
        'socks',
        'pens'
        ]

print (shopping_cart[::2])
print ('slicing the shopping cart by 2')
shopping_cart[2] = 'guns'
print (shopping_cart)
print ('added guns in shopping car')
print (old_cart)
print ('printing contents in original old_cart')
old_cart[1] = shopping_cart[1]
print (shopping_cart)
print ('added the contents of 1 in shopping cart to old cart')
print (old_cart)
print ('now printing the old cart to see wether the 1st slot is taken by glasses')
print (shopping_cart)
print ('printing to see if he 1st content in shopping cart has been changed or replaced.')
print (shopping_cart)
print (old_cart)
old_cart = shopping_cart [:]
print ('just copied all slices of shopping car to old cart')
print (shopping_cart)
print (old_cart)
print ('assigned the old_cart contents back')
old_cart = [
        'weights', 
        'dumbels', 
        'socks',
        'pens'
        ]
print (old_cart)
old_cart = shopping_cart
print ('just assigned shopping car to old cart')
old_cart[1] = 'dragonfly'
print ('just changed 2nd slot in old cart with knives')
shopping_cart[2] = 'lizard'
print (shopping_cart)
print (old_cart)

matrix = [
    [1,[0,3,4],3],
    [2,4,6],
    [7,8,9]
]

print(str(matrix[0][1][2]) + str(matrix[1][2]))

basket = [1,2,3,4,5]

#adding # inserting # 
basket.append(100)
basket.insert(3, 200)
basket.extend([4000, 50000, 9874])
basket.pop()
basket.pop(2)
basket.remove(4)
#basket.clear()
print (basket)
print (basket.index(2, 0, 4))
print (basket.index(2))