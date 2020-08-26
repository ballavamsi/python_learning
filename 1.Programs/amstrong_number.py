def checkIfNumberIs(type,num):
    multiplynum = 3
    total = 0
    divnum = num
    if type == 'armstrong':
        multiplynum = 3
    elif type == 'narcistic':
        multiplynum = 4

    while divnum > 0:
        #print(divnum)
        modnum = divnum % 10
        #print(modnum)
        total += modnum **3
        #print(total)
        divnum = int(divnum / 10)
        #print(divnum)
    if total == num:
        return  True
    else:
        return False

print(checkIfNumberIs('armstrong',152))
print(checkIfNumberIs('armstrong',153))


print(checkIfNumberIs('narcistic',152))
print(checkIfNumberIs('narcistic',153))