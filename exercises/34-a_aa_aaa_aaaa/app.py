digit = int(input("Your digit : "))

def addEmAll(n):
    value = 0
    for i in range(1,digit+1):
        value += (digit ** i)
    
    return value

print(addEmAll(digit))
