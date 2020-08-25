import math

def pf(data):
    print(data)

pf(math.pi)
pf(math.ceil(math.pi))

pf(math.log(10))
pf(math.exp(1))
pf(math.pow(3,2))

pf(math.factorial(3))

#pf(math.abs(-5.4))

pf(math.fabs(-5))

pf(8 / 3)


def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

pf(isEven(3))
pf(isEven(12))

minutes = 63

def getHours(num):
    return str( int(num / 60)) + ":" + str(num % 60)

pf(getHours(63))