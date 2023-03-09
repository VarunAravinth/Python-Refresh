''' find the even numbers in a list 1-10'''

list_1 = [1,2,3,4,5,6,7,8,9,10]

# OR

list_1 = [i for i in range(1,11)]

# usual way
sol = []
for number in list_1:
    if number %2 ==0:
        sol.append(number)
# print(sol)

# using list comprehension to find even numbers
sol = [ i for i in range(1,11) if i%2==0 ]

# in case we need to write an else 
sol = [ i if i%2==0 else "odd"  for i in range(1,11)  ]
print(sol)
    

''' home work problem : write a function, to find odd number 
input for the function is a list
1. without list comprehension
2. using list comprehension
'''


'''
find the square of list of numbers
'''
input_li = [1,1,2,3,4,6,7,8,9,9,10,10]
''' without using for loop/while'''

def square(number):
    return number * number

def even(number):
    if number%2==0:
        return number

sol = map(square, input_li)
print(list(sol))

sol = filter(even, input_li)
print(list(sol))


