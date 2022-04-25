n = int(input('nhap n'))
count =0
sum = 0
ls = []
if n<0:
    print("nhap lai n")
else:
    for i in range(1,n+1):
        if n%i ==0:
            ls.append(i)

print(ls)
print(len(ls))
for i in ls:
    sum += i

print(sum)