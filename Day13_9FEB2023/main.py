# garbage collection

a= [1,2,3] # memlocation 0x100

b = a # memlocation 0x100

# object -> [1,2,3]
# reference b

print(a)
print(b)

a = 10

#object - 10 0x110
#reference a

# garbage collection happens at the end of your program
# garbage -acts when an object loses all its reference

# garbage collection is automatic

# del -> ?
del a # deletes the reference to the object (a)
print(b)

del b


class Sample:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __del__(self):
        print('del is called - {}'.format(self))

a= Sample('a')
b = Sample('b') #0x200
del b

#reference delete -> del
#object -> garbage collector

# 1. del does nothing but deletes the reference to the object
#2. Python calls __del__ method right before the garbage collector destroys the object.
