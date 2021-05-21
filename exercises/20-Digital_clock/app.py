#Complete the function to return how many hrs and min are displayed on the 24th digital clock.
def digital_clock(n):
    hour = n // 60
    minute = (n - (hour * 60))
    return hour, minute

#Invoke the function with any interger (seconds after midnight)
print(digital_clock(150))
