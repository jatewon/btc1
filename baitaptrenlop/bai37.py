import math
n = int(input('nhap n'))
ls =[]
for i in range(1,n+1):
    ls.append(i)
sum = 0
max = int((math.sqrt(8*n+1) -1)/2)
for i in range(1,max+1):
    sum += i

print(sum)
 