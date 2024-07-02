Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ###tuple assignment###
>>> 
>>> (a,b)=(2,'app')
>>> print(a)
2
>>> 
>>> print(b)
app
>>> 
>>> a=b
>>> b=a
>>> 
>>> print(a)
app
>>> 
>>> print(b)
app
>>> b=a
>>> print(b)
app
>>> 
>>> (a,b,c)=(2,3,4)
>>> print(a)
2
>>> 
>>> print(b)
3
>>> 
>>> print(c)
4
>>> 
>>> a=b
>>> b=c
>>> c=a+b
>>> 
>>> print(a)
3
>>> print(b)
4
>>> print(c)
7
