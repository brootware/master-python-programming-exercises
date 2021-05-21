#Complete the function to return the first digit to the right of the decimal point.
def first_digit(num):
    afterDecimalIndex = int(str(num).find('.')) + 1
    num = int(str(num)[afterDecimalIndex])
    return num

#Invoke the function with a positive real number. ex. 34.33
print(first_digit(1.79))