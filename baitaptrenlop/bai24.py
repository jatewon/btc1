
n= int(input('nhap n'))
def tongso(n):
    total = 0
    for i in range(1,n):
        total = total + n%10
        n = int(n/10)
        return total
#print(tongso(n))
def daonguoc(n):
    while (n != 0):
        print(n % 10, end="")
        n = n // 10  

daonguoc(n)