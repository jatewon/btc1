import math
n = int(input('nhap n'))
sumvt = 0
for i in range(1,n+1):
    sumvt += i**3
sumvp = int(((n**2)*((n+1)**2))/4)
print("ve trai :{0}".format(sumvt))
print("ve trai :{0}".format(sumvp))