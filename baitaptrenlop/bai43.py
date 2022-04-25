from operator import index


n1 = 0
n2 = 1
ls = []
n = int(input('nhap so Fi cam tim'))
for i in range(2,40):
    n3 = n1 + n2
    ls.append(n3)
    n1= n2
    n2 = n3

for i in ls:
    if n == ls.index(i):
        print(i)

