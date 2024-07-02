a=3
b=10
c=36
d=89
f=123
g='a'
print(a+b)
print(c+d)
try:
    
    print(d+g)
except:
    print('forgot that on')
    print(d+f)
    print(d-a)


a=int(input('age-'))
b=int(input('number-'))
c=float(input('family-'))
d=str(input('people-'))

print(a+b)
print(a-b)
print(a*c)
try:
    print(d-c)
except:
    print('learning error')
