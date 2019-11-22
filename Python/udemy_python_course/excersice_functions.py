def highest_even(num1):
    num1.sort()
    for i in range(len(num1)):
        if (num1[-1]) % 2 == 0:
            return num1[-1]
        else: 
            num1.pop()
print(highest_even([10,2,3,254,8,989,678,444,555,2,2,243,54,3,52,54,3,5]))

def top_number(num2):
    evenlist = []
    for item in num2:
        if item % 2 == 0:
           evenlist.append(item)
    return max(evenlist)

print(top_number([10,2,3,254,8,989,678,444,555,2,2,243,54,3,52,54,3,5]))

print (max(('python','rajesh','three','six','nine'), key=len))

                # if a variable is not part of a def then it doesn't have access to it and vice versa. This is called as scope

total = 0

def count(total):
                #global total
    total += 1
    return total

count(total)
count(total)
print (count(count(count(total))))