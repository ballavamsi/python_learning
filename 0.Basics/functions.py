def multiply(x,y):
    z = 3
    if x < 0 or y < 0:
        print("values should be greater than 0")
    else:
        print(z ** 3)
        return x * y

print(multiply(10,20))
print(multiply(20,-1))
# will throw error
# print(z)


#complex functions
inputArray = [1,2,3,4] # output [1,4,9,16]
def square(li):
    fli = []
    for i in range(0, len(li)):
        result = li[i] ** 2
        fli.append(result)
    return fli

print(square(inputArray))


