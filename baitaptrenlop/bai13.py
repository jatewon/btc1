import math
day = int(input('nhap ngay'))
month = int(input('nhap thang'))
year = int(input('nhap nam'))
dayofweek = (day +2*month + (3*(month +1))/5 + year + (year/4))%7
if round(dayofweek)==0:
    print("chu nhat")
elif round(dayofweek) == 1:
    print('thu 2')
elif round(dayofweek) == 2:
    print('thu 3')
elif round(dayofweek) == 3:
    print('thu 4')
elif round(dayofweek) == 4:
    print('thu 5')
elif round(dayofweek) == 5:
    print('thu 6')
elif round(dayofweek) == 6:
    print('thu 7')
