Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #operators
>>> #addition
>>> print(9+10)
19
>>> a=23
>>> b=30
>>> print(a+b)
53
>>> #subtraction
>>> print(90-30)
60
>>> #multipication
>>> print(34*56)
1904
>>> #division:it always gives decimal
>>> 45/5
9.0
>>> #integer or floor division:it gives integer value
>>> 45//5
9
>>> #modules(remainder)[%]
>>> 46%5
1
>>> #powers
>>> 3**2
9
>>> 5**3
125
>>> 25**2
625
>>> #1) above all examples are relating to the arthmetical operators
>>> #2)assigment operators
>>> a=5
>>> a+=4
>>> print(a)
9
>>> #subtraction
>>> x=8
>>> x-=4
>>> print(x)
4
#multipication
a=4
a*=5
print(a)
20
#all operation done by same

#3)unary operators
#unary plus
a=10
print(+a)
10
#unaryminus
print(-a)
-10

#4) relationship operator
#equals(==)
a=5
b=5
print(a==b)
True
#not equal(!=)
a=10
b=5
print(a!=b)
True
#greater than(>)
a=5
b=2
print(a>b)
True
#less than
print(a<b)
False
#greater than equal to (>=)
print(a>=b)
True
#less than equal to
print(a<=b)
False

#Logical operations
#logic and :both are true it become true otherwise false
a=True
b=False
print(a and b)
False
#logic or: if any one is true it will become true otherwise false
print(a or b)
True
# logic not : reverse if true-false,false-true
a=True
print(not True)
False
a=false
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    a=false
NameError: name 'false' is not defined. Did you mean: 'False'?
a= False
print(not False)
True
