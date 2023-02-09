# basic file concepts

''' Files on most modern file system are composed 3 main parts
file header -> metadata -> size, type, file_name, last_modified and so on.
data -> contents of the file
EOF -> End of File : special character which denotes end of line
'''

''' operations done in file with python
1. open a file, either read or write
2. work with the file
3. close the file
'''

# create file handle
f = open("Day13_9FEB2023\\file_1.txt",'r')
print('writable - read -------------')
print(f.writable())
data = f.read(6) # read the complete file
print(data)
data1 = f.read()
print(data1)
print(f.tell()) # says the current pointer position

f.seek(6) # moves the pointer to the byte specified
data5 = f.read()
print(data5)

f.seek(0)

# ------------------------------sample 2
print(' readline method -----------------------')
data = f.readline() # reads one line, until \n is encountered
print(f.tell())
print(data)

f.seek(0)
# --------------- sample 3 ------------------------
print(' readlines method -----------------------')
data = f.readlines()
print(data)

f.close()


# r -> used to read data from a file
# w -> write data to a file, overwrites 
# a -> writes data to the file, at the end, existing content is retained
# b -> used to work with binary/image

f2 = open(r"Day13_9FEB2023\\file_2.txt", 'w')

string = 'sample string'
f2.write(string)
f2.close()


f3 = open(r"Day13_9FEB2023\\file_2.txt", 'w')
string = 'sample string2\n'
f3.write(string)
f3.close()

f4 = open(r"Day13_9FEB2023\\file_2.txt", 'a')
string = 'sample string3\n'
f4.write(string)
f4.close()


f5 = open(r"Day13_9FEB2023\\file_2.txt", 'a')
print(f5.writable())
string = 'sample string3\n'
f5.writelines(['line 1\n', 'line 2\n', 'line 3\n', 'line 4\n', 'line 5\n'])
print(f5.writable())
f5.close()


f5 = open(r"Day13_9FEB2023\\file_2.txt", 'r')
if f5.writable():
    string = 'sample string3\n'
    f5.writelines(['line 1\n', 'line 2\n', 'line 3\n', 'line 4\n', 'line 5\n'])
    print(f5.writable())
    f5.close()
else:
    print('file is write-protected')

# wr

