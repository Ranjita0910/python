##for decreasing pattern
##row will same but column only change
###outer loop represent-row
## inner loop represent -column
## row,variable(a,n)

n=4
for a in range(n):
    for b in range(a,n):
        print('$%',end=' ')
    print()

