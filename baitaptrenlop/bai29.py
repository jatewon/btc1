import math
print("Celcius  Fahrenhenit")
for i in range(0,10+1):
    print("{0}   {1}".format(i,((9*i)/5) + 32))
print("Fahrenhenit  Celcius")
for i in range(32,42+1):
    print('{0}     {1}'.format(i,(5*(i-32)/9)))