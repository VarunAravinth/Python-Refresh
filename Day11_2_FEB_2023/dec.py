# simple scenario

def magic(func):
    def inner():
        print('magic decoration')
        func()
    return inner


@magic
def simple():
    print('simple function')

simple()


# practical example


def find_second_char(func):
    def inner(string,c):
        if string.find(c) !=-1:
            new_index = string.find(c) +1
        return func(string,c,new_index)

    return inner


@find_second_char
def find_char(string,c,start_index=0):
    return string.find(c,start_index)

print(find_char('samples','s'))



