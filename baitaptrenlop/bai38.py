n = int(input('nhap so tien '))
for i in range(0,int(n/1000)):
    for j in range(0,int(n/2000)):
        for k in range(0,int(n/5000)):
            if(i*1000 + j*2000 + k*5000 == n):
                print('{0}:1000 {1}:2000 {2}:5000'.format(i,j,k))