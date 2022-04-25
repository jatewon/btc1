r = float(input('nhap lai xuat'))
p = float(input('nhap tien von'))
n = int(input('nhap thoi han gui'))
print('Nam   Von')
for i in range(1,n+1):
    print(" {0}  {1}".format(i,round(p*(1 +r)**i)))