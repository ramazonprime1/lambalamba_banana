#OOP or Object Oriented Programming

class PlayerCharacter:
    red_team = True
    bulldozer = 'vehicle'
    def __init__(self, name, age):
        if (self.red_team):
            self.name = name #attributes
            self.age = age
    
    def shout(self):
        print (f'my name is {self.red_team}')
        print (f'my name is {self.bulldozer}')
        print (f'my name is {self.name}')
        return 'done'
    
player1 = PlayerCharacter('cindy', 44)
player2 = PlayerCharacter('Jonathon', 32)
player2.attack = 20

""" help(player1.attack)
print (player2.attack)
 """
print (player1.age)
print (type(player1))
print (player2.name)
print (player2.shout())

numbers = {'cat1':4, 'cat2':5, 'cat3': 6}

print (list(numbers))
print (sorted(numbers))

#is admin / S@NAdm1n

#RFE is asking for a client letter. I've already provided that to the attorney at Cognier.
