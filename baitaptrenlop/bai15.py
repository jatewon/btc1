day = int(input('nhap ngay '))
month = int(input('nhap thang'))
year = int(input('nhap nam'))
s = day
for i in range(1,month):
    if i ==4 or i ==6 or i== 9 or i ==11:
        s += 30
    elif i ==2:
        s += 28 + ((year %4 ==0 and year %100) or (year%400==0))
    else:
        s+=31
print(day,month,year)
print('ngay thu:',s)