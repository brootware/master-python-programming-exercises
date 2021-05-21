#Complete the function "digits_sum" so that it prints the sum of a three digit number.
def digits_sum(num):
    num = int(str(num)[0]) + int(str(num)[1]) + int(str(num)[2])
    return num


#Invoke the function with any three-digit-number
#You can try other three-digit numbers if you want
print(digits_sum(123))