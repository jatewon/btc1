sokW = int(input("nhap so kW tieu thu:"))
if sokW <=100:
    print("chi phi {0}".format(sokW*500))
elif sokW >100 and sokW <=250:
    print("chi phi {0}".format(sokW*800))
elif sokW >250 and sokW <=350:
    print("chi phi {0}".format(sokW*1000))
elif sokW >350:
    print("chi phi {0}".format(sokW*1500))