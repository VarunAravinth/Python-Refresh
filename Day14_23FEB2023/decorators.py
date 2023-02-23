# you decorate a function, without changing the function's definition
# decorating -> add addditional features to the function without changing the definition

def decorator(func):
    def inner():
        print('---decoration----')
        func()
    return inner


@decorator
def magic():
    print('magic')

# longer way
# magic = decorator(magic)
# magic()


magic()