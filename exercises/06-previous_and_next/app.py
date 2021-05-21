#Complete the function to return the previous and next number of a given numner.".
def previous_next(num):
    previousNum = num-1
    nextNum = num+1
    return previousNum, nextNum


#Invoke the function with any interger at its argument. 
print(previous_next(179))