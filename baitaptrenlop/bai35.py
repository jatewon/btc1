import math
n =int(input('nhap n'))
ls =[]
def  sont(n):
    if n<2:
        return False
    so = int(math.sqrt(n))
    for i in range(2,so+1):
        if (n%i==0):
            return False
    return True
for i in range(2,n+1):
        if(sont(i)):
            ls.append(i)
if(sont(n)==True):
    print("la snt")
else:
    print("ko la snt")
    print('sont gan nhat :{0}'.format(ls[-1]))


