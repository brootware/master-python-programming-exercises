#Complete the function to return the respective number of the century
#HINT: You may need to import the math module.
import math

def century(year):
    # year = year / 100
    # year = math.ceil(year)
    # return year
    return (year // 100) + 1

#Invoke the function with any given year. 
print(century(2020))