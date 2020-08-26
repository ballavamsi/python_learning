li = []

def fibanocci(minnum,maxnum):
    a = 0
    b = 1
    c = 0
    while maxnum >= c:
        c = a + b
        if maxnum < c:
            break
        temp = b
        b = c
        a = temp
        if c >= minnum and c <= maxnum:
            li.append(c)

fibanocci(100,1000)
print(li)