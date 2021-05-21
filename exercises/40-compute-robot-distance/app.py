import math

origin = [0,0]

while True:
    uInput = input("Key in ur instructions separated by white space : ").upper()
    if not uInput:
        break
    movement = uInput.split(' ')
    direction = movement[0]
    steps = int(movement[1])
    if direction == "UP":
        origin[0] += steps
    elif direction == "DOWN":
        origin[0] -= steps
    elif direction == "RIGHT":
        origin[1] += steps
    elif direction == "LEFT":
        origin[1] -= steps
    else:
        pass

print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))
