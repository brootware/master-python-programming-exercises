#Complete the function to return the total cost in dollars and cents of N cupcakes. 
#Remember you can return multiple parameters => return a, b
def total_cost(d,c,n):
    totalCost = ((d * 100) + c) * n
    d = totalCost // 100
    c = totalCost % 100
    return d,c

#Invoke the function with three intergers: cost(dollars and cents) & number of cupcakes.
print(total_cost(15,22,4))
