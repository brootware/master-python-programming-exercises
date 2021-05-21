uInput = input("Input : ")

charList = [i for i in uInput if i.isalpha()]
upperCase = 0
lowerCase = 0

for c in charList:
    if c.isupper():
        upperCase += 1
    elif c.islower():
        lowerCase += 1

print("UPPER CASE : {}. LOWER CASE : {}".format(upperCase,lowerCase))
