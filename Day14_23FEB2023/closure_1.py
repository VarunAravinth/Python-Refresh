

# inner function closes in all the parent function() environmental variables.
def outer_fun():
    message = 'hello' # --> free variable

    def inner_func():
        print(message)
    
    return inner_func

a = outer_fun()

a()
