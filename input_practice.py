Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name=input('what is your name:')
what is your name:vani
>>> age=input('waht is your age:')
waht is your age:28
>>> age=int(input("what is your age'))
...               
SyntaxError: unterminated string literal (detected at line 1)
>>> age=int(input('what is age'))
...               
what is age:25
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    age=int(input('what is age'))
ValueError: invalid literal for int() with base 10: ':25'
>>> print(age*4)
...               
28282828
>>> ptint(int(age*3))
...               
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    ptint(int(age*3))
NameError: name 'ptint' is not defined. Did you mean: 'print'?
>>> print(f'good morning{name}')
...               
good morningvani
>>> 
>>> age=int(input('your age:'))
...               
your age:28
>>> print(age*4)
...               
112
>>> a=int(input('a:'))
... b=int(input('b:'))
...               
SyntaxError: multiple statements found while compiling a single statement
>>> print(a)
...               
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
a=int(input('a:'))
              
a:23
b=int(input('b:'))
              
b:44
print(a+b)
              
67
print(b-a)
              
21
print(a*b)
              
1012
print(b/a)
              
1.9130434782608696
print(b%a)
              
21
print(a==b)
              
False
