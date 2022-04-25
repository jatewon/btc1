for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            if x**2 + y**2 == z**2:
                print("({0} ,{1} ,{2})".format(x,y,z))