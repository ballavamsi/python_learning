def isAmstrongNumber(num):
    total = 0
    divnum = num
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

print(isAmstrongNumber(152))