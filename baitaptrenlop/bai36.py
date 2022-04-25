import math
sstr =''
n = int(input('nhap n'))
def sont(n):
    if n<2:
        return False
    so = int(math.sqrt(n))
    for i in range(2,so +1):
        if (n%i==0):
            return False
    return True

for i in range(2,n+1):
    if sont(i):
        sstr = sstr +str(i) + ' '

print(sstr)