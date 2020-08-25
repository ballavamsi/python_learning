string = 'Hello world this is vamsi'
#string[start: end: skip]

print(string[5:10:1])

print(string[::-1])

a = 1
b = '1'
c = '5g'
# will throw error bcz int doesn't have isdigit
# print(a.isdigit())
print(b.isnumeric())
print(c.isdecimal())

windex = string.find('w')

print(string[windex:])
print(string.title())

print(" --------------- ")
# trying to reverse each word
strSplit = string.split(' ')
#for i in range(0,len(strSplit)):
for i in range(len(strSplit)):
    strSplit[i] = strSplit[i][::-1]

print(' '.join(strSplit).swapcase())
