basket = [1, 6, 3, 4, 5, 2]
bowl = ['a', 'b', 'c', 'd', 'e', 'f']
name = ('rajesh kommisetty')

print (bowl.index('b'))
print (name.index('j'))

print ('s' in name)
print (4 in basket)

print (name.count('s'))

#basket.sort()

print (sorted(basket))
basket.sort()
basket.reverse()
print (basket[::-1])
print (basket)
#print(list(range(45,250)))
#print(list(range(250)))

name = ' '
full_sentence = name.join(['hi', 'my', 'name', 'is', 'rajesh'])

print (full_sentence)

#list unpacking

a, b, c, *other, e = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print (a, b, c,)
print (other)
print (e)

#dictionary

dicttionary = {
    'a': ['z','x','c'],
    'b': 2,
    'x': 3
}

print (dicttionary['b'])

#Dictionary

user = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 32
}

print (user.get('age', 44))

user2 = dict(name = 'johnjohn')

print (user2)

print ('greet' in user)

print (name)

print ('hello' in user.values())
print ('age' in user.keys())
print ('a' in 'age')