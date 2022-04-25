tuso = int(input('nhap tu so'))
mauso = int(input('nhap mau so'))
def ucln(a,b):
    while(b>0):
        r = int(a%b)
        a = b
        b = r
    return a
print("tu so {0} mau so {1}".format(tuso,mauso))
tsrutgon = tuso/ucln(tuso,mauso)
msrutgon = mauso/ucln(tuso,mauso)
print('Rut gon : {0}/{1}'.format(tsrutgon,msrutgon))