
diemchuan = float(input('nhap diem chuan'))
diemmon1 = float(input('nhap diem1:'))
diemmon2 = float(input('nhap diem2:'))
diemmon3 = float(input('nhap diem3:'))
diemkhuvuc = (input('nhap diem khu vuc A,B,C:'))
if diemkhuvuc == 'A':
    diemkhuvuc =2
elif diemkhuvuc == 'B':
    diemkhuvuc = 1
elif diemkhuvuc == 'C':
    diemkhuvuc = 0.5
diemdoituong = int(input('nhap diem doi tuong'))
if diemdoituong == 1:
    diemdoituong = 2.5
elif diemdoituong ==2:
    diemdoituong = 1.5
elif diemdoituong == 3:
    diemdoituong = 1

diemthisinh = diemmon1 + diemmon2 + diemmon3 + diemdoituong + diemkhuvuc

if  diemthisinh>= diemchuan:
    print("dat: ",diemthisinh)
else:
    print('rot ',diemthisinh)