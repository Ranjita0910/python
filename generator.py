def topten():
    n=11
    while n<=20:
        sq=n*n
        yield sq
        n+=1
values=topten()
for i in values:
    print(i)
