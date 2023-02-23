# Functions behave as objects

def sample():
    return 'sample'


a = sample()
print(a) # sample

b = sample
print(b)
print(sample)

print(b())

# you can store functions in a variable/data structure
li = []
li.append(sample)

li.append(5)
li.append(6)

print(li[0]())


#you can pass a function as an argument/parameter

def superior(func): # func = sample
    func()


def sample2():
    print('sample2')


superior(sample2)


# you can return a function

def magic():

    def inner():
        print('inner')
    return inner


a = magic()
a()
