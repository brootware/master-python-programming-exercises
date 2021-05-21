#Complete the function to return the tens digit and the ones digit of any interger.
def two_digits(digit):
    leftDigit = int(digit / 10)
    rightDigit = int(digit % 10)
    return leftDigit, rightDigit
   


#Invoke the function with any interger as its argument.
print(two_digits(79))