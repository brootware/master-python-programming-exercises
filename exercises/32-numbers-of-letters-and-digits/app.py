uInput = (input("Input : "))

charList = [i for i in uInput if i.isalnum()]
Letters = 0
Digits = 0

for c in charList:
    if c.isalpha():
        Letters += 1
    elif c.isnumeric():
        Digits += 1

print("LETTERS : {}. DIGITS : {}".format(Letters,Digits))


