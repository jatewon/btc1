a = int(input('nhap vao a'))
b = int(input('nhap vao b'))
def gcd(a,b):
    while(b>0):
        r = int(a%b)
        a = b
        b = r
    return a
def bcnn(a,b):
    return int((a*b)/gcd(a,b))

print(gcd(a,b))
print(bcnn(a,b))