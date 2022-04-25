n = int(input('nhap so n'))
for i in range(1,n):
    sum =0
    for j in range(1,i):
        if i%j ==0:
            sum += j
    if sum /2.0 == i:
        print(i)