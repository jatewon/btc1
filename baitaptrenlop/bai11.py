from math import radians
import random
print("nhap b-d-k")
human = input()
computer = random.randint(0,2)
if computer == 0:
   computer = 'b'
if computer == 1:
   computer = 'd'
if computer == 2:
   computer = 'k'
print("ban chon",human)
print('may chon:',computer)

