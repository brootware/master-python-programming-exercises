uInput = input()
arr = uInput.split(',')

def genListTuple(arr):
    genList = list(arr)
    genTuple = tuple(arr)

    return genList, genTuple

print(genListTuple(arr))