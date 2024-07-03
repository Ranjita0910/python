Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
5
5
a=input()
s
5
5
###user input
input('enter a value:)
      
SyntaxError: unterminated string literal (detected at line 1)
a=input('enter a value:')
      
enter a value:5
type(a)
      
<class 'str'>

b=('message=')
      
a=input('enter a value:')
      
enter a value:ranju
typr(a)
      
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    typr(a)
NameError: name 'typr' is not defined. Did you mean: 'type'?
>>> type(a)
...       
<class 'str'>
>>> b=input('name:')
...       
name:ranju
>>> c=input('age=')
...       
age=24
>>> 
>>> 
>>> ###conditional statement
...       
>>> if True
...       
SyntaxError: expected ':'
>>> if True:
...         print('hai')
...         print('bye')
... 
...       
hai
bye
>>> if False:
...         print('hello')
...         print('world')
... 
...       
>>> 
>>> ###space is matter
...       
>>> 
>>> x=int(input('enter a value:'))
...       
enter a value:
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    x=int(input('enter a value:'))
ValueError: invalid literal for int() with base 10: ''
