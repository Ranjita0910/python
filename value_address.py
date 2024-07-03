Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=2
>>> address=id(2)
>>> print(address)
140712402033112
>>> b=2
>>> address=id(b)
>>> print(address)
140712402033112
>>> c=a
>>> address=id(c)
>>> print(address)
140712402033112
>>> text='hello'
>>> address=id(text)
>>> print(address)
1519536087056
>>> c='ranju'
>>> address=id(c)
>>> print(c)
ranju
>>> print(address)
1519543733488
>>> number=09
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> number=56
>>> address=id(number)
>>> print(address)
140712402034840
