#PEP8 -> coding standard


s='hello world, today is a nice day'
char = 'z'

def return_char_count(string,c):
    sol = 0
    for ch in s:
        if ch == c:
            sol += 1
    
    if sol == 0:
        return -1

    return sol

print(return_char_count(s,char))


def starrer(number):
    for num in range(0, number):
        for s in range(0, number-num):
            print(" ", end='')
        
        for i in range(0, num+1):
            print('*', end=' ')

        print()

starrer(5)

li = ['hello', 'world', 'hello']

string= ' '.join(li)
print(string)

string = 'hello'
for i in range(len(string)-1,-1,-1):
    print(string[i])




