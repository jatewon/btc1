
day = int(input('nhap day'))
month = int(input('nhap month'))
year = int(input('nhap year'))
def ngayhople(day):
    if day==0 or day>31:
        return
def namhople(year):
    if year<0:
      return
def thanghople(month):
    if month<1 or month >12:
     return
def tinhngayhomsau(day,month,year):
    ngayhople(day)
    namhople(year)
    thanghople(month)
    if (day == 30 and month == 4 ) or (day == 30 and month == 6 ) or (day == 30 and month == 9 ) or (day == 30 and month == 11) or (day == 28 and month ==2):
        print(1,month+1,year)
    elif (day == 31 and month == 1 ) or(day == 31 and month == 3) or (day == 31 and month == 5) or (day == 31 and month == 7) or (day == 31 and month == 8) or (day == 31 and month == 10) :
        print(1,month+1,year) 
    elif (day == 31 and month == 12):
        print(1,1,year+1)
    else:
        print(day+1,month,year)

def tinhngayhomtruoc(day,month,year):
    ngayhople(day)
    namhople(year)
    thanghople(month)
    if day ==1 and month == 3:
       return (28,month-1,year) 
    elif (day ==1 and month == 2) or (day ==1 and month == 4) or (day == 1 and month == 8 ) or (day ==1 and month == 6) or (day ==1 and month == 9) or (day ==1 and month == 12):
       return(31,month-1,year)
    elif (day == 1 and month == 5 ) or (day == 1 and month == 7 ) or (day == 1 and month == 10) or (day == 1 and month ==12):
       return(30,month-1,year)
    if day ==1 and month ==1:
        return (31,12,year-1)
    else:
       return(day-1,month,year)

chon = int(input('lua chon 1: ngay truoc 2:ngay sau'))
if chon ==1:
    print(tinhngayhomtruoc(day,month,year))
elif chon == 2:
    print(tinhngayhomsau(day,month,year))
else:
    print("chon 1 trong 2 thoi")

        