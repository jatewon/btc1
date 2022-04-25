import math
"""xC = float(input("nhap xC"))
yC = float(input("nhap yC"))"""
print("nhap 3 canh tam giac")
a = float(input("nhap canh a"))
b = float(input("nhap canh b"))
c = float(input("nhap canh c"))
p = (a+b+c)/2
S = math.sqrt(p*(p-a)*(p-b)*(p-c))
if (a**2 + b**2 ==c**2) or (b**2 + c**2 ==a**2) or (a**2 + c**2 ==b**2):
    print("tam giac vuong")
elif(a==b and b==c):
    print("tam giac đều")
elif(a*a > b*b+c*c or b*b > a*a+c*c or c*c > a*a+b*b):
    print("tam giác tù")
else:
    print("tam giác nhọn")
print("diện tích là:",S)