uInput = list(input("Input : ").split(' '))

deDupe = dict.fromkeys(uInput)
deDupe = ' '.join(deDupe)
print(deDupe)