#li = []
# should be using below instead of above
li = list()

def fibanocci(maxnum):
    a = 0
    b = 1
    c = 0
    while maxnum >= c:
        c = a + b
        if maxnum <= c:
            break
        temp = b
        b = c
        a = temp
        li.append(c)

fibanocci(100)
print(li)