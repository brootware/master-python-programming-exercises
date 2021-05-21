#Complete the function to return the tens digit of a given interger
def tens_digit(num):
    tensDigit = int(str(num)[-2])
    return tensDigit


#Invoke the function with any interger.
print(tens_digit(170))