# flatten the list

# input
li = [1,2,3,4,[55,66,77,88,99,[555,666,777],89,90],6,7,8]

#expected output - [1,2,3,4,55,66,77,88,99,555,666,777,89,90,6,7,8]



# recursive solution

sol= []

def flatten(li):
    for obj in li:
        if isinstance(obj,list):
            return flatten(obj) # flatten([55,66,77,88,99,[555,666,777],89,90])  #flatten([555,666,777])
        else:
            sol.append(obj)

    return (sol)


# print(flatten(li))

li =[1,2,3,4,5,6,6,6,7,7,9,9,9,2,3,4,10]
m = list(set(li))

sol = []
for obj in li:
    if obj not in sol:
        sol.append(obj)

print(sol)


