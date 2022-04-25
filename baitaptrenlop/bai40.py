for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            if x + y + z == 100 and (15*x +9*y +z ==300):
                print('({0},{1},{2})'.format(x,y,z))