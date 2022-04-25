import math
hour = int(input('nhap hour'))
week = math.floor(hour/(24*7))
day = math.floor((hour - week*24*7)/24)
hourc = math.floor(hour -week*24*7 - day*24)
print('{0} tuan {1} ngay {2} gio'.format(week,day,hourc))
