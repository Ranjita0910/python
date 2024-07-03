Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ####dictionary
>>> 
>>> d={1:'a',2:'b',3:'d'}


>>> print(d)
{1: 'a', 2: 'b', 3: 'd'}
>>> 
>>> type(d)
<class 'dict'>
>>> 
>>> ###editing###
>>> 
>>> d={1:'a',2:'b',3:'d'}
>>> d[1]='h'
>>> print(d)
{1: 'h', 2: 'b', 3: 'd'}
>>> 
>>> d[1]=d[1]+3
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    d[1]=d[1]+3
TypeError: can only concatenate str (not "int") to 

sd
>> d={1:'a',2:'b',3:'d'}
print(d[1])
a=d[1]
print(a)
