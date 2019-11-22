'''def test_generator_function():
    for i in range(10):
        yield i

for item in test_generator_function():
    print (item)

def fibonacci(n): #using generator
    a = b = 1
    for i in range(n):
        yield a
        a,b = b, a + b
def fibonacci(n): #not using generator
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a+b
    return result

for x in fibonacci(1000):
    print (x)

'''

def generator_function():
    for i in range(3):
        yield i

gen = generator_function()
print(next(gen))
print(next(gen))
print(next(gen))
#print(next(gen)) #this will generate a StopIteration error.
print(gen)