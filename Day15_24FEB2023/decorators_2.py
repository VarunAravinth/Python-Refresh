# takes in a function as a argument
# adds some functionality without changing the definition

#First class -> decorators


def smart_divide(func):
    def inner(a,b):
        if b > a:
            return 'oops cannot divide'
        else:
            return func(a,b)

    return inner

@smart_divide
def divide(a,b):
    ''' it divided two variables'''
    return a/b

# divide = smart_divide(divide) # instead of @syntax

print(divide(10,5))
print(divide(5,10))




