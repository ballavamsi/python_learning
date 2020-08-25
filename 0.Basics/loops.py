for i in range(0,10):
    print(i)

print("----------------")
names = ['hi','this','is','vamsi']
for i in names:
    print(i)

print("----------------")
for i in range(0,len(names)):
    print(str(i) + ' :' + names[i])
print("----------------")
print("Skipping elements will print only even values the number we specified will be skipped")
for i in range(0, 10, 2):
    print(i)
print("----------------")
for i in range(5):
    print(i)

# while loop
print("----------------")
counter = 0
while counter < len(names):
    print(names[counter])
    counter += 1

# get from index
print("----------------")
print(names[0:2])

# reverse
print("----------------")
print(names[3:0:-1])

# last element
print(names[-1])

print("----------------")

# simple loop test
sen = 'hWelDo Sowksok Sowkd Sowksewd'

for w in sen:
    print(w)

senList = list(sen)
for w in range(0,len(senList)):
    senList[w] = senList[w].lower()

print(senList)
print(''.join(senList))
