def square(li):
    for element in li:
        yield element*element


li = [i for i in range(1,6)]

x = square(li)

print(x)
print(next(x))
print(next(x)) 
print(next(x)) 
print(next(x))
print(x.__next__()) 
print(x.__next__()) 