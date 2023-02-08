Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> b=20
>>> a+b
30
>>> a='s'
>>> b='m'
>>> a+b
'sm'
>>> a= int(10)
>>> b=int(20)
>>> a+b
30
>>> a='s'
>>> a=str('s')
>>> b=str('m')
>>> a+b
'sm'
>>> a='hello'
>>> b=' world'
>>> a+b
'hello world'
>>> a=10
>>> b='world'
>>> a+b
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a+b
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> int.__add__(1,2)
3
>>> int.__add__(1)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    int.__add__(1)
TypeError: expected 1 argument, got 0
>>> s='sample'
>>> len(s)
6
>>> str.__len__(s)
6
s=100
s
100
del s
s
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    s
NameError: name 's' is not defined
