uInput = input("Input : ").split(',')

numList = [int(x) for x in uInput]
for i in numList:
    if i % 5 == 0:
        print(i)
