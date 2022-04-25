n= int(input('nhap n'))

def tachthuaso(n):
    i = 2
    ls = []
    while n>1:
        if n%i==0:
            n = n/i
            ls.append(i)
        else:
            i = i+1
    if (len(ls)==0):
        ls.append(n)
    return ls

ls = tachthuaso(n)
size = len(ls)
sb = ""
for i in range(0,size -1):
    sb = sb + str(ls[i])+ 'x'
sb = sb + str(ls[size -1])
print("kq {0}".format(sb))