n = int(input('nhap n'))
sum = 0
m =n
while m>0:
    so = m%10
    sum += so **3
    m //= 10
if n == sum:
    print("so armstrong")
else:
    print("ko phai")
