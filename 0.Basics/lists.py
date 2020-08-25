a = [1,2,3,'abadsf','asd',[2,3,4,43]]
b = [1,3,4,5]
print(max(b))
b.reverse()
print(b)

a.insert(0,31)
print(a)
print(a.index('asd'))

print(3 in a)
print(4 in a)


## each word should have +
testData = ["+d++=3=+s+","f++d+"]

def SimpleFormat(data):
    data = data
    for i in range(len(data)):
        if data[i].isalpha():
            if i == 0 or i == len(data)-1:
                return False
            if data[i-1] != '+' or data[i+1] != '+':
                return False
    return True

print("-------------")
print(SimpleFormat(testData[0]))
print(SimpleFormat(testData[1]))