import math
hour1 = int(input('nhap gio 1'))
mins1= int(input('nhap phut 1'))
second1 = int(input('nhap giay 1'))
hour2 = int(input('nhap gio 2'))
mins2= int(input('nhap phut 2'))
second2 = int(input('nhap giay 2'))

sum1 = hour1*60*60 + mins1*60 + second1
sum2 = hour2*60*60 + mins2*60 + second2
gio = math.floor((sum2 -sum1)/3600)
phut = math.floor(((sum2-sum1)-3600*gio)/60)
giay = math.floor((sum2 -sum1) -gio*3600 -phut*60)
print(' hien thi thoi gian:{0} gio {1} phut {2} giay'.format(gio,phut,giay))
