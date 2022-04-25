print("giai he phuong trinh 2 an")
print("nhap a1,b1,c1")
a1 =int(input())
b1 = int(input())
c1 = int(input())
print("nhap a2,b2,c2")
a2 = int(input())
b2 = int(input())
c2 = int(input())
D = a1*b2 -a2*b1
Dx = c1*b2 -c2*b1
Dy = a1*c2 - a2*c1
if D ==0:
    print("he phuong trinh vo no")
elif D !=0:
    print("x = ",Dx/D," ",'y = ',Dy/D) 
