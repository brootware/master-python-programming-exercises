pWord = input("Password : ").split(',')

for n in pWord:
    if len(n) >= 6 and len(n) <= 12:
        for i in n:
            if i.islower() and i.isupper() and i.isdigit() and i == '$' or i == '@' or i == '#' or i == '%':
                print(n)