#Complete the fuction to return the swapped digits of a given two-digit-interger.
def swap_digits(num):
    leftDigit = int(num / 10)
    rightDigit = int(num % 10)
    newDigit = str(rightDigit) + str(leftDigit)
    return newDigit
   
   
#Invoke the function with any two digit interger as its argument
print(swap_digits(79))