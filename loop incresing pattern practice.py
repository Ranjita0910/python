##for increasing pattern
##row will same but column only change
###outer loop represent-row
## inner loop represent -column
##row+1

n=4
for a in range(n):
    for b in range(a+1):
        print('#',end=' ')
    print()
